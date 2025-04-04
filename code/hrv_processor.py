# HRV Processing logic placeholder

import numpy as np

def compute_rmssd(rr_intervals):
    """
    Compute RMSSD from a list of RR intervals.
    """
    diff = np.diff(rr_intervals)
    squared = diff ** 2
    rmssd = np.sqrt(np.mean(squared))
    return rmssd
