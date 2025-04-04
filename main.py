from code.ear_detection import compute_ear_from_video
from code.hrv_processor import process_hrv_data
from code.steering_entropy import calculate_entropy
from code.cnn_lstm_model import load_model_and_predict
from code.fusion_engine import fuse_modalities

def main():
    print("🔍 Starting fatigue detection pipeline...")

    # Step 1: EAR Detection (Simulated or real)
    ear_features = compute_ear_from_video("data/sample_ear.csv")

    # Step 2: HRV Metrics Extraction
    hrv_features = process_hrv_data("data/hrv_example.csv")

    # Step 3: Steering Entropy
    se_score = calculate_entropy("data/steering_entropy.csv")

    # Step 4: Fuse all inputs
    feature_vector = fuse_modalities(ear_features, hrv_features, se_score)

    # Step 5: Load trained model and predict fatigue
    prediction = load_model_and_predict(feature_vector)

    print(f"🧠 Fatigue Prediction: {'Drowsy' if prediction == 1 else 'Alert'}")

if __name__ == "__main__":
    main()
