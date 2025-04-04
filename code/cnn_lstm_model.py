"""
Module: CNN + LSTM Model
Builds a hybrid deep learning model for fatigue classification.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense

def build_model(input_shape=(30, 64, 64, 1)):
    """
    Constructs and compiles a CNN-LSTM model.
    
    Args:
        input_shape (tuple): (frames, height, width, channels)
    
    Returns:
        keras.Model: Compiled model
    """
    model = Sequential()
    model.add(TimeDistributed(Conv2D(32, (3, 3), activation='relu'), input_shape=input_shape))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    model.add(TimeDistributed(Flatten()))
    model.add(LSTM(64))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


if __name__ == "__main__":
    # Build the model and print summary
    model = build_model()
    model.summary()
