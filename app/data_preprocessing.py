import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib




def load_and_preprocess_data(filepath):
    # Cargar el conjunto de datos
    data = pd.read_csv(filepath)
    
    # Revisión inicial
    print("Data info before cleaning:")
    print(data.info())
    
    # Limpieza de datos
    # Ejemplo: eliminación de filas con valores nulos en la columna objetivo

    data['total_bedrooms'].fillna(data['total_bedrooms'].mean(),inplace=True)

    variables_outliers = ['total_rooms','total_bedrooms','population','households']
    percentiles = [11212.11000000003, 2216.270000000004, 5805.830000000002, 1982.6600000000035]

    # Reemplazamos los outliers por el percentil 99

    for i in variables_outliers:
        data[i] = [(percentiles[variables_outliers.index(i)]) if x > (percentiles[variables_outliers.index(i)])
                else x for x in data[i]]
    

    # Hacemos dummies con la variable ocean_proximity
    data_cl = pd.get_dummies(data , columns=['ocean_proximity'])

    data_cl['rooms_household'] = data_cl['total_rooms'] / data_cl['households']
    data_cl['population_household'] = data_cl['population'] / data_cl['households']
    
    X = data.drop('median_house_value', axis=1) 

    scaler = joblib.load('app/Scaler.pkl')

    X_preprocessed = scaler.trans(X)
    
    return X_preprocessed