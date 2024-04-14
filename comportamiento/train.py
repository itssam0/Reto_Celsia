from data_preparation import load_and_preprocess_data, split_data, features, targets
import data_preparation
from model import create_model
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

def train_and_save_model(filepath):
    data = load_and_preprocess_data(filepath)
    X_train, y_train, X_val, y_val, scaler_features, scaler_targets = split_data(data)
    model = create_model(X_train.shape[1])  # Cambio aquí para adaptarse a la red densa
    model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_val, y_val))
    model.save('model.keras')

    # Guardar también los escaladores para usar en la predicción
    pd.to_pickle(scaler_features, 'scaler_features.pkl')
    pd.to_pickle(scaler_targets, 'scaler_targets.pkl')

def predict_new_data(model_path, new_data_filepath):
    model = load_model(model_path)
    
    scaler_features = pd.read_pickle('scaler_features.pkl')
    scaler_targets = pd.read_pickle('scaler_targets.pkl')

    # Cargar los nuevos datos
    new_data = pd.read_csv(new_data_filepath)
    new_data['Fecha'] = pd.to_datetime(new_data['Fecha'], errors='coerce')
    new_data = data_preparation.add_time_features(new_data)

    # Asegúrate de que los datos estén completos y preparados adecuadamente
    if 'Medidor [W]' not in new_data.columns:
        raise ValueError("The 'Medidor [W]' column is missing from the new data.")
    
    # Verificar y preparar las características para la predicción
    new_data_prepared = new_data[features]  # Esto asume que todas las características necesarias están presentes

    # Transformar las características con el scaler usado en el entrenamiento
    new_data_scaled = scaler_features.transform(new_data_prepared)

    # Realizar predicciones con el modelo
    predictions = model.predict(new_data_scaled)
    
    # Asegurar que no haya predicciones negativas
    predictions = np.maximum(predictions, 0)

    # Invertir la transformación del escalador para los objetivos
    predictions_inversed = scaler_targets.inverse_transform(predictions)

    # Crear DataFrame para los resultados
    result_columns = targets
    results = pd.DataFrame(predictions_inversed, columns=result_columns)

    # Combinar 'Fecha' y 'Medidor [W]' con los resultados de las predicciones
    results_final = pd.concat([new_data['Fecha'], new_data['Medidor [W]'], results], axis=1)

    return results_final

if __name__ == "__main__":
    filepath = 'https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/consumo_casa.csv'
    new_data_filepath = 'https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/new_data.csv'
    train_and_save_model(filepath)
    predicted_matrix = predict_new_data('model.keras', new_data_filepath)
    predicted_matrix.to_csv('predicted_results.csv', index=False)
    print(predicted_matrix)
