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
    names = 'TIME,VPV,IPV,PPV,V,I,P,IL,PL'.split(',')
    df = pd.read_csv(f, sep = sep, names = names)

    vdf = df.loc[:,['TIME', 'PPV', 'P',  'PL']]
    vdf.PPV = vdf.PPV.apply(strip_unit)
    vdf.PL = vdf.PL.apply(strip_unit)
    vdf.P = vdf.P.apply(strip_unit)

    ppv_sum = np.sum(np.array(vdf.PPV)) / INPUT_SAMPLE_RATE
    p_sum = np.sum(np.array(vdf.P)) / INPUT_SAMPLE_RATE
    pl_sum = np.sum(np.array(vdf.PL)) / INPUT_SAMPLE_RATE

    p_is_charged = vdf.P > 0.0
    p_is_discharged = vdf.P < 0.0    
    p_charge_sum = np.sum(np.array(vdf.P)[p_is_charged]) / INPUT_SAMPLE_RATE
    p_discharge_sum = np.sum(np.array(vdf.P)[p_is_discharged]) / INPUT_SAMPLE_RATE

    t_now = vdf.TIME.iloc[-1]

    text = f'TIME {t_now}'
    text += f' SOLAR {ppv_sum:.1f} Wh'
    text += f' +BAT {p_charge_sum:+.1f} Wh'
    text += f' -BAT {p_discharge_sum:+.1f} Wh'
    text += f' BAT {p_sum:+.1f} Wh'
    text += f' LOAD {pl_sum:.1f} Wh'
    text += f' SYS {-ppv_sum + p_sum + pl_sum:+.1f} Wh'
    
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
