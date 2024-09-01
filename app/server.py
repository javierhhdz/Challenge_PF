
# Imports
from fastapi import FastAPI
import pickle, uvicorn, os
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from data_preprocessing import load_and_preprocess_data

# Cargar y preprocesar datos

model = joblib.load('app/random_forest_regression_model.pkl')



class HousingFeatures(BaseModel):

    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    median_house_value: float
    ocean_proximity: object


app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Housing price model API'}

@app.post("/predict/")
def predict(features: HousingFeatures):
    input_data = np.array([[features.longitude, features.latitude, features.housing_median_age,
                            features.total_rooms, features.total_bedrooms, features.population,
                            features.households, features.median_income, features.median_house_value, features.ocean_proximity]])
    X_preprocessed = load_and_preprocess_data('housing.csv')
    prediction = model.predict(X_preprocessed)
    return {"predicted_price": prediction[0]}


if __name__ == "__main__":     
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)