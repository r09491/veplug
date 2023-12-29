#!/usr/bin/env python3

import sys
import argparse

import pandas as pd
import numpy as np

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta

def str2date(value):
    return datetime.strptime(value, '%H:%M')

def strip_unit(value):
    return float(value[:-1])


def plot_volts(time, vpv, v, ppv, p, pl):
        dformatter = mdates.DateFormatter('%H:%M')
        #dformatter.set_tzinfo(self.tzinfo)

        fig, axes = plt.subplots(nrows=3, figsize=(12,12))

        text = f'Victron MPPT'
        fig.text(0.5, 0.0, text, ha='center', fontsize='x-large')

        axes[0].fill_between(time, vpv, color='blue', linewidth=4,label='PPV', alpha=0.5)
        axes[0].axhline(33.5, color='blue', linewidth=2, label='VMP')
        axes[0].axhline(39.4, color='blue', linewidth=2, linestyle=':', label='VOC')
        axes[0].legend(loc="upper left")
        axes[0].grid(which='major', linestyle='-', linewidth=2, axis='both')
        axes[0].grid(which='minor', linestyle='--', linewidth=1, axis='x')
        axes[0].minorticks_on()
        title = f'Panel #'
        title += f' mean:{np.mean(vpv):.0f}V max:{np.max(vpv):.0f}V'
        axes[0].set_title(title, fontsize='x-large')
        axes[0].set_ylabel('Volts [V]')
        axes[0].xaxis.set_major_formatter(dformatter)

        axes[1].plot(time, v, color='red', linewidth=4, label='BAT')
        axes[1].axhline(12.1, color='magenta', linewidth=6, label='EMPTY')
        axes[1].axhline(12.8, color='magenta', linewidth=4, label='CHARGED')
        axes[1].axhline(13.8, color='red', linewidth=2, linestyle=':', label='FLOAT')
        axes[1].axhline(14.4, color='red', linewidth=3, linestyle=':', label='ABSORP')
        axes[1].legend(loc="upper left")
        axes[1].grid(which='major', linestyle='-', linewidth=2, axis='both')
        axes[1].grid(which='minor', linestyle='--', linewidth=1, axis='x')
        axes[1].minorticks_on()
        title = f'Battery #'
        title += f' max:{np.max(v):.2f}V min:{np.min(v):.2f}V'
        axes[1].set_title(title, fontsize='x-large')
        axes[1].set_ylabel('Volts [V]')
        axes[1].xaxis.set_major_formatter(dformatter)

        axes[2].plot(time, ppv, color='blue', linewidth=4, label='PANEL', alpha=0.9)
        axes[2].fill_between(time, ppv, color='black', label='LOST', alpha=0.3)
        axes[2].fill_between(time, p+pl, color='green', label='BAT+LOAD', alpha=0.5)
        axes[2].fill_between(time, p, color='red', label='BAT', alpha=0.7)
        axes[2].legend(loc="upper left")
        axes[2].grid(which='major', linestyle='-', linewidth=2, axis='both')
        axes[2].grid(which='minor', linestyle='--', linewidth=1, axis='x')
        axes[2].minorticks_on()
        title = f'Power #'
        title += f' Panel max:{np.max(ppv):.0f}W sum:{np.sum(ppv)/60:.1f}Wh'
        title += f' | Battery max:{np.max(p):.0f}W'
        title += f' | Load max:{np.max(pl):.0f}W sum:{np.sum(pl)/60:.1f}Wh'
        axes[2].set_title(title, fontsize='x-large')
        axes[2].set_ylabel('Watts [W]')
        axes[2].xaxis.set_major_formatter(dformatter)

        fig.tight_layout(pad=2.0)

        ##fig.savefig(name)
        ##plt.close(fig) 
        plt.show()

        
def show_volts(f = sys.stdin):
    sep = '\t'
    names = 'TIME,VPV,IPV,PPV,V,I,P,IL,PL'.split(',')
    df = pd.read_csv(f, sep = sep, names = names)

    """ The timestamps """
    time = np.array(df.TIME.apply(str2date))
    """ The panel voltage samples """
    vpv = np.array(df.VPV.apply(strip_unit))    
    """ The battery voltage samples """
    v = np.array(df.V.apply(strip_unit))
    """ The panel power samples """
    ppv = np.array(df.PPV.apply(strip_unit))    
    """ The battery power samples """
    p = np.array(df.P.apply(strip_unit))    
    """ The battery power samples """
    pl = np.array(df.PL.apply(strip_unit))    

    plot_volts(time, vpv, v, ppv, p, pl)

    return 0


def parse_args():
    parser = argparse.ArgumentParser(description='Plot MPPT Volts')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    show_volts()
    return 0

if __name__ == '__main__':
    sys.exit(main())
