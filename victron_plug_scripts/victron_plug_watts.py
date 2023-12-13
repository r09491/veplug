#!/usr/bin/env python3

import sys
import argparse
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

V_SAMPLES = 60 # 1 hour
V_LOAD_OFF = 12.1 # V
V_LOAD_DISCHARGE = 12.8 #V

def strip_unit(value):
    return float(value[:-1])

def estimate_load_off(f = sys.stdin):
    sep = '\t'
    names = 'TIME,VPV,IPV,PPV,V,I,P,VL,IL,PL'.split(',')
    df = pd.read_csv(f, sep = sep, names = names).tail(V_SAMPLES)

    vldf = df.loc[:,['TIME','VL', 'PL', 'PPV', 'P']]

    """ The timestamps """
    t = np.array(vldf.TIME)
    
    """ The battery voltage samples """
    vl = np.array(vldf.VL.apply(strip_unit))

    """ The power samples """
    pl = np.array(vldf.PL.apply(strip_unit))
    p = np.array(vldf.P.apply(strip_unit))
    ppv = np.array(vldf.PPV.apply(strip_unit))

    
    """ Calculate the means  """
    pl_mean = np.mean(pl)
    p_mean = np.mean(p)
    ppv_mean = np.mean(ppv)

    text = f'TIME {t[-1]}'
    text += f' SOLAR {ppv_mean:.1f} W'
    text += f' BAT {p_mean:+.1f} W'
    text += f' LOAD {pl_mean:.1f} W'
    text += f' SYS {-ppv_mean + p_mean + pl_mean:.1f} W'
    text += f' VL {vl[-1]:.2f} V'    


    if vl[0] < V_LOAD_DISCHARGE:
        
        """ Forecast LOAD OFF time for discharge """

        samples = len(vl)
        vl_minutes = np.arange(samples)
        fit = np.polyfit(vl_minutes, vl, 1)
        line = np.poly1d(fit)

        """ Find the minute when to stop loading in the next 24h """
    
        load_off_minute = None
        for first_minute in range(samples, 23*samples, samples):
            """ The minutes of the next period """
            next_minutes = vl_minutes + first_minute
            """ The estimates of the next period """
            next_volts = line(next_minutes)
            """ The values larger than the load off """
            checked_minutes = next_minutes[next_volts > V_LOAD_OFF]
            if len(checked_minutes) < samples:
                load_off_minute = checked_minutes[-1]
                break

        if load_off_minute is not None:
            text += f' LOAD OFF {load_off_minute/60:.1f} h'

            load_off_time = datetime.strptime(t[-1], "%H:%M") + \
                timedelta(minutes = int(load_off_minute))
            text += f' @ {load_off_time.strftime("%H:%M")}'

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
