#!/usr/bin/env python3

import sys
import argparse
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

def strip_unit(value):
    return float(value[:-1])

V_RATE_PERIOD = 15 # Minutes
V_LOAD_OFF = 12.1 # V
V_LOAD_DISCHARGE = 12.8 #V

def estimate_load_off(f = sys.stdin):
    sep = '\t'
    names = 'TIME,VPV,IPV,PPV,V,I,P,VL,IL,PL'.split(',')
    df = pd.read_csv(f, sep = sep, names = names).tail(V_RATE_PERIOD)

    vldf = df.loc[:,['TIME','VL', 'PL', 'PPV', 'P']]
    vldf.VL = vldf.VL.apply(strip_unit)
    vldf.PL = vldf.PL.apply(strip_unit)
    vldf.P = vldf.P.apply(strip_unit)
    vldf.PPV = vldf.PPV.apply(strip_unit)

    pl_mean = np.mean(np.array(vldf.PL))
    p_mean = np.mean(np.array(vldf.P))
    ppv_mean = np.mean(np.array(vldf.PPV))


    vl_start = vldf.VL.iloc[0]
    vl_now = vldf.VL.iloc[-1]
    vl_delta = vl_now - V_LOAD_OFF

    
    t_start = vldf.TIME.iloc[0]
    t_now = vldf.TIME.iloc[-1]
    t0 = datetime.strptime( t_start, '%H:%M')
    t1 = datetime.strptime( t_now, '%H:%M')
    dt = (t1 - t0).total_seconds()

    
    text = f'TIME {t_now}'
    text += f' SOLAR {ppv_mean:.1f} W'
    text += f' BAT {p_mean:.1f} W'
    text += f' LOAD {pl_mean:.1f} W'
    text += f' VL {vl_now:.2f} V'    


    if vl_now < V_LOAD_DISCHARGE and dt > 0.0 and vl_delta > 0.0:
        discharge_rate = (vl_now - vl_start) / dt
        if discharge_rate < 0.0:
            load_off_secs = abs(vl_delta / discharge_rate)
            load_off_time = t1 + timedelta(seconds = load_off_secs)

            text += f' LOAD OFF {load_off_secs/3600:.1f} h @ {load_off_time.strftime("%H:%M")}'
        
    print(text)

    return 0


def parse_args():
    parser = argparse.ArgumentParser(description='Esimate MPPT load off time')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    estimate_load_off()
    return 0

if __name__ == '__main__':
    sys.exit(main())
