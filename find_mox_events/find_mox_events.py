#Jaron Whittington
from scipy.signal import find_peaks_cwt
import pandas as pd
import numpy as np

def find_mox_events(mox, times, start_cut = 160, jump_cut_off= 300, peak_min = 60, sure_peak = 1000, std_window = 50,
                    peak_window_min = 50, peak_window_max = 60, num_std = 3):
    """
    Takes the mox sensor data from a session and returns the 
    times and magnitude of the 'mox events'
    
    Args:
        mox (list): List of the raw data from the sensor
        times (list): List of the corresponding timestamps
        start_cut (int): Number of data points to cut off from the start. Default 160
        jump_cut_off (int): How large a jump in data that identifies bad data. Default 300
        peak_min (int): Minimum standard deviation that can identify an event. Default 60
        sure_peak (int): Standard deviation, above which, is surely a mox event. Default 1000
        std_window (int): Width (in number of data points) of window used to calculate rolling standard deviation. Default 50
        peak_window_min (int): Smallest number of data points in which we expect to see concurrent peaks. Default 50
        peak_window_max (int): Number larger than peak_window_min, the largest width we want our peak finder to look for. Default 60
        num_std (int): Number of standard deviations above the mean we wish to identify as an event. Default 3
    Returns:
        dict: A dictionary with keys being timestamps and magnitudes,
        with the keys being correlated.
    """
    #create rolling standard deviation 
    std = list(pd.Series(mox).rolling(std_window).std())
    #cut off beginning noise
    mox = mox[start_cut:]
    times = times[start_cut:]
    std = std[start_cut:]
    #cut off noise at end
    last = mox[0]
    i = -1
    for value in mox:
        i += 1
        if (value - last) > jump_cut_off:
            mox = mox[:i]
            times = times[:i]
            std = std[:i]
            break
        last = value
        
    #identify peaks from the rolling standard deviation 
    peaks = find_peaks_cwt(std, np.arange(peak_window_min,peak_window_max))
    #identify peaks that are 'true' peaks
    #to identify a 'true' peak, we check to see if the peak is unusually high for the particular session (over num_std above the mean)
    #the peak must be at least above the peak_min, and if the peak is above the sure_peak it is gauranteed to be a 'true' peak
    #if the peak is due to the sensor dropping to 0, we throw out that peak
    tpeaks = []
    for peak in peaks:
        if ((std[peak] > (np.mean(std)+num_std*np.std(std)) and std[peak] > peak_min) or std[peak] > sure_peak) and mox[peak] > 0:
            tpeaks.append(peak)
    mox_events = {}
    mox_events['timestamps'] = times[tpeaks]
    mox_events['magnitude'] = std[tpeaks]
    
    return mox_events
    
