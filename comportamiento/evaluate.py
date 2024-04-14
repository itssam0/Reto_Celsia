from tensorflow.keras.models import load_model
from data_preparation import load_and_preprocess_data, split_data

def evaluate_model(filepath, model_path):
    data = load_and_preprocess_data(filepath)
    _, _, X_test, y_test = split_data(data)
    model = load_model(model_path)
    
    loss = model.evaluate(X_test.values.reshape((X_test.shape[0], X_test.shape[1], 1)), y_test)
    print(f'Evaluation Loss: {loss}')

if __name__ == "__main__":
    filepath = 'https://raw.githubusercontent.com/itssam0/Reto_Celsia/main/consumo_casa.csv'  # Path to the data file
    model_path = 'model.h5'
    evaluate_model(filepath, model_path)