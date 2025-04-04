# Drowsy-Driver-Detection

A hybrid CNN-LSTM based fatigue detection system using EAR, HRV, and Steering Entropy

### 📊 Sample Data

| 📁 File                  | 📝 Description                                  |
|-------------------------|-------------------------------------------------|
| `sample_ear.csv`        | Simulated eye aspect ratio data over time       |
| `hrv_example.csv`       | RR-intervals for HRV metric extraction          |
| `steering_entropy.csv`  | Sample steering angles to compute entropy       |


### 🧠 Core Code Modules

| 📄 File                 | ⚙️ Description                                                  |
|------------------------|------------------------------------------------------------------|
| `ear_detection.py`     | Computes Eye Aspect Ratio (EAR) using 6 eye landmark points      |
| `hrv_processor.py`     | Extracts HRV metrics like RMSSD, LF/HF ratio, and pNN50          |
| `steering_entropy.py`  | Calculates entropy of steering angle variations                  |
| `cnn_lstm_model.py`    | Defines and compiles the CNN-LSTM hybrid fatigue model           |
| `fusion_engine.py`     | Combines EAR, HRV, and SE scores to generate fatigue probability |


### 📊 Figures Overview

| Figure | Description |
|--------|-------------|
| `figure2_steering_entropy_hist.png` | Steering entropy pattern (Alert vs Fatigue) |
| `figure4_bar_metrics.png` | Bar chart of Accuracy, Precision, Recall, F1 |
| `figure6_radar_chart.png` | Radar chart showing model performance |
| `figure7_feature_importance.png` | Feature contribution to fatigue detection |
| `figure8_clustering_view.png` | Clustering visualization of Alert vs Fatigue |
| `figure9_pca_projection.png` | PCA projection of feature space |
