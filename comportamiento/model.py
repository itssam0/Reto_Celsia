from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def create_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(8)  # 8 targets to predict
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model