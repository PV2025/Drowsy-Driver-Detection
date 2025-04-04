# 📊 Exploratory Analysis – Drowsy Driver Detection

This file contains simple data visualizations and sanity checks on the multimodal inputs used in the fatigue detection system.

---

## 📋 Table of Contents

- [1. Load Sample EAR Data](#1-load-sample-ear-data)
- [2. HRV Data Exploration](#2-hrv-data-exploration)
- [3. Steering Entropy Distribution](#3-steering-entropy-distribution)
- [4. Final Notes](#4-final-notes)

---

## 1. Load Sample EAR Data

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and plot EAR over time
df_ear = pd.read_csv('../data/sample_ear.csv')
plt.plot(df_ear['Time'], df_ear['EAR'])
plt.title("EAR Drop Over Time")
plt.xlabel("Time (s)")
plt.ylabel("EAR Value")
plt.grid(True)
plt.show()

df_hrv = pd.read_csv('../data/hrv_example.csv')
df_hrv[['RMSSD', 'LF_HF']].plot()
plt.title("HRV Metrics Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.grid(True)
plt.show()

df_se = pd.read_csv('../data/steering_entropy.csv')
plt.hist(df_se['Entropy'], bins=10, edgecolor='black')
plt.title("Steering Entropy Distribution")
plt.xlabel("Entropy")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


---

### ✅ What to Do:
1. **Delete everything currently in `analysis_notes.md`**.
2. **Paste this full block exactly**.
3. **Commit changes** with a message like:  


You’ll now have a fully structured, clean, professional exploratory report ready for any reviewer, teammate, or professor.

Let me know when you're ready for Phase 6, Commander. 🫡
