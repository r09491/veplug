__doc__ = """
Defines filter tables for converting the serial VE stream
"""
from datetime import datetime
from veserial.vemappings import PID, CS, MPPT, OR, ERROR


def mul1(left, right, info):
    scale, form, unit = info
    return f'{float(left)*scale:{form}}{unit}'

    
def mul2(left, right, info):
    scale, form, unit = info
    return f'{float(left)*float(right)*scale:{form}}{unit}'
    
    
def div2(left, right, info):
    scale, form, unit = info
    return f'{float(left)/float(right)*scale:{form}}{unit}'


def num1(left, right, info):
    return f'{int(left)}'

def copy(left, right, info):
    return f'{left}'

def pid(left, right, info):
    return f'{PID[left]}'

def cs(left, right, info):
    return f'{CS[left]}'

def mppt(left, right, info):
    return f'{MPPT[left]}'

def or_(left, right, info):
    return f'{OR[left]}'

def err(left, right, info):
    return f'{ERROR[left]}'

def time(left, right, info):
    scale, form, unit = info
    return datetime.now().strftime(f'{form}')


FULL_CONVERTER = {
    'TIME': [time,  None,  None,     None, '%H:%M', None],
    'PID':  [pid,  'PID',  None,     None,  None, None],
    'FW':   [mul1,  'FW',  None, 0.010000, '.2f',   ''],
    'SER#': [copy,'SER#',  None,     None,  None, None],
    'V':    [mul1,   'V',  None, 0.001000, '.2f',  'V'],
    'I':    [mul1,   'I',  None, 0.001000, '.2f',  'A'],
    'P':    [mul2,   'V',   'I', 0.000001, '.0f',  'W'],
    'VPV':  [mul1, 'VPV',  None, 0.001000, '.2f',  'V'],
    'IPV':  [div2, 'PPV', 'VPV', 1000.000, '.2f',  'A'],
    'PPV':  [mul1, 'PPV',  None, 1.000000, '.0f',  'W'],
    'CS':   [cs,    'CS',  None,     None,  None, None],
    'MPPT': [mppt,'MPPT',  None,     None,  None, None],
    'OR':   [or_,   'OR',  None,     None,  None, None],
    'ERR':  [err,  'ERR',  None,     None,  None, None],
    'LOAD': [copy,'LOAD',  None,     None,  None, None],
    'VL':   [mul1,   'V',  None, 0.001000, '.2f',  'V'],
    'IL':   [mul1,  'IL',  None, 0.001000, '.2f',  'A'],
    'PL':   [mul2,   'V',  'IL', 0.000001, '.0f',  'W'],
    'H19':  [mul1, 'H19',  None, 1.000000, '.0f', 'Wh'],
    'H20':  [mul1, 'H20',  None, 10.00000, '.0f', 'Wh'],
    'H21':  [mul1, 'H21',  None, 1.000000, '.0f',  'W'],
    'H22':  [mul1, 'H22',  None, 10.00000, '.0f', 'Wh'],
    'H23':  [mul1, 'H23',  None, 1.000000, '.0f',  'W'],
    'HSDS': [mul1,'HSDS',  None, 1.000000, '.0f',  'd']}


LATEST_CONVERTER = {
    'TIME': [time,  None,  None,     None, '%H:%M', None],
    'V':    [mul1,   'V',  None, 0.001000, '.2f',  'V'],
    'I':    [mul1,   'I',  None, 0.001000, '.2f',  'A'],
    'P':    [mul2,   'V',   'I', 0.000001, '.0f',  'W'],
    'VPV':  [mul1, 'VPV',  None, 0.001000, '.2f',  'V'],
    'IPV':  [div2, 'PPV', 'VPV', 1000.000, '.2f',  'A'],
    'PPV':  [mul1, 'PPV',  None, 1.000000, '.0f',  'W'],
    'VL':   [mul1,   'V',  None, 0.001000, '.2f',  'V'],
    'IL':   [mul1,  'IL',  None, 0.001000, '.2f',  'A'],
    'PL':   [mul2,   'V',  'IL', 0.000001, '.0f',  'W']}


PRODUCT_CONVERTER = {
    'PID':  [pid,  'PID',  None,     None,  None, None],
    'FW':   [mul1,  'FW',  None, 0.010000, '.2f',   ''],
    'SER#': [copy,'SER#',  None,     None,  None, None]}


HISTORY_CONVERTER = {
    'H19':  [mul1, 'H19',  None, 1.000000, '.0f', 'Wh'],
    'H20':  [mul1, 'H20',  None, 10.00000, '.0f', 'Wh'],
    'H21':  [mul1, 'H21',  None, 1.000000, '.0f',  'W'],
    'H22':  [mul1, 'H22',  None, 10.00000, '.0f', 'Wh'],
    'H23':  [mul1, 'H23',  None, 1.000000, '.0f',  'W'],
    'HSDS': [mul1,'HSDS',  None, 1.000000, '.0f',  'd']}


def convert( data, info):
    keys = [k for k in info.keys() if info[k] is not None]
    values = [info[k][0](left = data[info[k][1]] if info[k][1] is not None else None,
                         right = data[info[k][2]] if info[k][2] is not None else None, 
                         info = info[k][3:]) for k in keys]
    return dict(zip(keys, values))

