#Lectura de datos 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

data = pd.read_csv('https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/consumo_casa.csv')

# Convertir la columna de fecha
data['Fecha'] = pd.to_datetime(data['Fecha'])

# Extraer características del tiempo
data['Year'] = data['Fecha'].dt.year
data['Month'] = data['Fecha'].dt.month
data['Day'] = data['Fecha'].dt.day
data['Hour'] = data['Fecha'].dt.hour
data['Minute'] = data['Fecha'].dt.minute

# Normalizar los datos
scaler = MinMaxScaler()
features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Medidor [W]']
targets = ['Refrigerator', 'Clothes washer', 'Clothes Iron', 'Computer', 'Oven', 'Play', 'TV', 'Sound system']
data[features + targets] = scaler.fit_transform(data[features + targets])

# Dividir los datos
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
X_train, y_train = train_data[features], train_data[targets]
X_test, y_test = test_data[features], test_data[targets]





