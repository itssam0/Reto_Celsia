import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Definir las variables globales para características y objetivos
features = ['Year', 'Month', 'Day', 'Hour', 'Minute',  'Medidor [W]']
targets = ['Refrigerator', 'Clothes washer', 'Clothes Iron', 'Computer', 'Oven', 'Play', 'TV', 'Sound system']

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    
    # Convertir la columna de fecha
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = add_time_features(data)

    # Interpolar valores faltantes
    data.interpolate(method='linear', inplace=True)
    
    return data

def add_time_features(data):
    
    # Extraer características del tiempo
    data['Year'] = data['Fecha'].dt.year
    data['Month'] = data['Fecha'].dt.month
    data['Day'] = data['Fecha'].dt.day
    data['Hour'] = data['Fecha'].dt.hour
    data['Minute'] = data['Fecha'].dt.minute
    
    # Codificación cíclica para la hora
    #data['sin_hour'] = np.sin(2 * np.pi * data['Hour']/24.0)
    #data['cos_hour'] = np.cos(2 * np.pi * data['Hour']/24.0)
    
    return data


def split_data(data):
    scaler_features = MinMaxScaler()
    scaler_targets = MinMaxScaler()
    
    # Asegúrate de incluir todas las características en el escalado
    data[features] = scaler_features.fit_transform(data[features])
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    
    train_targets = scaler_targets.fit_transform(train_data[targets])
    train_data[targets] = train_targets
    test_data[targets] = scaler_targets.transform(test_data[targets])
    
    return train_data[features], train_data[targets], test_data[features], test_data[targets], scaler_features, scaler_targets
