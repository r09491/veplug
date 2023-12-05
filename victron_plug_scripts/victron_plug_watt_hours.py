#!/usr/bin/env python3

import sys
import argparse
import pandas as pd
import numpy as np

from datetime import datetime


def strip_unit(value):
    return float(value[:-1])


INPUT_SAMPLE_RATE = 60   # Apriori knowledge


def sum_power(f = sys.stdin):
    sep = '\t'
    names = 'TIME,VPV,IPV,PPV,V,I,P,VL,IL,PL'.split(',')
    df = pd.read_csv(f, sep = sep, names = names)

    vldf = df.loc[:,['TIME', 'PPV', 'P',  'PL']]
    vldf.PPV = vldf.PPV.apply(strip_unit)
    vldf.PL = vldf.PL.apply(strip_unit)
    vldf.P = vldf.P.apply(strip_unit)

    ppv_sum = np.sum(np.array(vldf.PPV)) / INPUT_SAMPLE_RATE
    p_sum = np.sum(np.array(vldf.P)) / INPUT_SAMPLE_RATE
    pl_sum = np.sum(np.array(vldf.PL)) / INPUT_SAMPLE_RATE

    t_now = vldf.TIME.iloc[-1]

    text = f'TIME {t_now}'
    text += f' SOLAR {ppv_sum:.1f} Wh'
    text += f' BAT {p_sum:.1f} Wh'
    text += f' LOAD {pl_sum:.1f} Wh'
    
    print(text)

    return 0


def parse_args():
    parser = argparse.ArgumentParser(description='Sum up power samples')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    sum_power()
    return 0

if __name__ == '__main__':
    sys.exit(main())
