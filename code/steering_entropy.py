"""
Module: Steering Entropy
Calculates entropy of steering angle behavior over a time window.
"""

import numpy as np

def compute_steering_entropy(steering_angles, bins=10):
    """
    Computes entropy of steering angle variations.
    
    Args:
        steering_angles (list or array): Recorded angles
        bins (int): Number of histogram bins
    
    Returns:
        float: Entropy score
    """
    hist, _ = np.histogram(steering_angles, bins=bins, density=True)
    hist = hist[hist > 0]
    entropy = -np.sum(hist * np.log2(hist))
    return entropy


if __name__ == "__main__":
    # Example input: simulated steering angles
    sample_angles = [2.3, 2.5, 2.7, 3.0, 3.5, 3.8, 4.0]
    
    entropy_score = compute_steering_entropy(sample_angles)
    print("Steering Entropy:", entropy_score)
