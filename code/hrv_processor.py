"""
Module: HRV Processor
Computes HRV features: RMSSD, LF/HF ratio, and pNN50.
"""

import numpy as np

def compute_rmssd(rr_intervals):
    """
    Root Mean Square of Successive Differences (RMSSD).
    """
    diff = np.diff(rr_intervals)
    return np.sqrt(np.mean(diff ** 2))

def compute_lfhf_ratio(lf_power, hf_power):
    """
    LF/HF power ratio.
    """
    return lf_power / hf_power if hf_power != 0 else float('inf')

def compute_pnn50(rr_intervals):
    """
    Percentage of NN intervals > 50ms apart.
    """
    diff = np.abs(np.diff(rr_intervals))
    count = np.sum(diff > 50)
    return 100.0 * count / len(diff)
