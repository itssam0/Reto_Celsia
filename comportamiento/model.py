from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def create_model(input_dim):
    model = Sequential([
        Dense(68, activation='relu', input_shape=(input_dim,)),  # Asegúrate de que input_dim refleje el nuevo número de características
        Dropout(0.2),
        Dense(68, activation='relu'),
        Dropout(0.2),
        Dense(8)  # 8 targets to predict
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model
