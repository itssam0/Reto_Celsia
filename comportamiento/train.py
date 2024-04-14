from data_preparation import load_and_preprocess_data, split_data, features, targets
import data_preparation
from model import create_model
import pandas as pd
from tensorflow.keras.models import load_model

def train_and_save_model(filepath):
    data = load_and_preprocess_data(filepath)
    X_train, y_train, X_val, y_val = split_data(data)
    model = create_model((X_train.shape[1], 1))
    model.fit(X_train.values.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train, epochs=10, batch_size=64, validation_data=(X_val.values.reshape((X_val.shape[0], X_val.shape[1], 1)), y_val))
    model.save('model.keras')

def predict_new_data(model_path, new_data_filepath):
    model = load_model(model_path)
    
    new_data = pd.read_csv(new_data_filepath)
    new_data['Fecha'] = pd.to_datetime(new_data['Fecha'])
    new_data = data_preparation.add_time_features(new_data)
    
    # Copia la columna 'Fecha' antes de filtrar por features
    fecha_column = new_data['Fecha'].copy()
    
    new_data = new_data[features]  # Utilizar directamente features importado de data_preparation
    predictions = model.predict(new_data.values.reshape((new_data.shape[0], new_data.shape[1], 1)))
    
    result_columns = ['Refrigerator', 'Clothes washer', 'Clothes Iron', 'Computer', 'Oven', 'Play', 'TV', 'Sound system']
    results = pd.DataFrame(predictions, columns=result_columns)
    results = pd.concat([fecha_column, results], axis=1)
    
    return results

if __name__ == "__main__":
    filepath = 'https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/consumo_casa.csv'
    new_data_filepath = 'https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/new_data.csv'
    train_and_save_model(filepath)
    predicted_matrix = predict_new_data('model.keras', new_data_filepath)
    print(predicted_matrix)
