#Jaron Whittington
import scipy.signal as sig
import pandas as pd
import numpy as np

def find_mox_events(mox, times):
    """
    Takes the mox sensor data from a session and returns the 
    times and magnitude of the 'mox events'
    
    Args:
        mox (list): list of the raw data from the sensor
        times (list): list of the corresponding timestamps
    Retruns:
        mox_events (dict): a dictionary with keys being the
        timestamp of event, and value being the magnitude.
    """
    mox = mox[160:]
    times = times[160:]
    last = mox[0]
    i = -1
    for value in mox:
        i += 1
        if (value - last) > 300:
            mox = mox[:i]
            times = times[:i]
            break
        last = value
    
    var = pd.Series(mox).rolling(50).std()
    var.fillna(0, inplace = True)
    peaks = sig.find_peaks_cwt(var, np.arange(50,60))
    tpeaks = []
    for peak in peaks:
        if ((var[peak] > (np.mean(var)+3*np.std(var)) and var[peak] > 60) or var[peak] > 1000) and mox[peak] > 0:#maybe change 1000
            tpeaks.append(peak)
    mox_events = {}
    for peak in tpeaks:
        mox_events[times[peak]] = var[peak]
    
    return mox_events
    
