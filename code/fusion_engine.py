"""
Module: Fusion Engine
Combines EAR, HRV, and SE to estimate drowsiness.
"""

def fuse_features(ear, hrv_score, entropy, weights=(0.4, 0.3, 0.3)):
    """
    Fuses three fatigue indicators using a weighted average.
    
    Args:
        ear (float): Eye aspect ratio
        hrv_score (float): Processed HRV feature (e.g., inverse RMSSD)
        entropy (float): Steering entropy score
        weights (tuple): Weights for (EAR, HRV, SE)
    
    Returns:
        float: Final fatigue score (0–1 range)
    """
    norm_ear = 1 - min(max(ear / 0.35, 0), 1)  # lower EAR = higher fatigue
    norm_hrv = min(hrv_score / 100.0, 1)
    norm_entropy = min(entropy / 3.0, 1)

    score = (weights[0] * norm_ear) + (weights[1] * norm_hrv) + (weights[2] * norm_entropy)
    return score


if __name__ == "__main__":
    final_score = fuse_features(ear=0.2, hrv_score=80, entropy=1.5)
    print("Fatigue Score:", final_score)
