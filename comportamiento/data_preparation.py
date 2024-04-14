import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


# Definir las variables globales para características y objetivos
features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Medidor [W]']
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
    
    return data


def split_data(data):
    
    # Normalizar los datos
    #features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Medidor [W]']
    #targets = ['Refrigerator', 'Clothes washer', 'Clothes Iron', 'Computer', 'Oven', 'Play', 'TV', 'Sound system']
    data[features + targets] = MinMaxScaler().fit_transform(data[features + targets])
    
    # Dividir los datos
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    return train_data[features], train_data[targets], test_data[features], test_data[targets]