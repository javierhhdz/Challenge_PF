# Challenge para implementar un modelo de predicción de precios de casas
========================================================================

The repository contains the files and results of the complete project for development, prediction, and deployment with FastAPI and Docker. The goal of the model is to predict the price of houses in a given California district based on 10 variables:: 

1. longitude: A measure of how far west a house is; a higher value is farther west
2. latitude: A measure of how far north a house is; a higher value is farther north
3. housingMedianAge: Median age of a house within a block; a lower number is a newer building
4. totalRooms: Total number of rooms within a block
5. totalBedrooms: Total number of bedrooms within a block
6. population: Total number of people residing within a block
7. households: Total number of households, a group of people residing within a home unit, for a block
8. medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars)
9. medianHouseValue: Median house value for households within a block (measured in US Dollars)
10. oceanProximity: Location of the house w.r.t ocean/sea

# Model creation

A notebook is generated with the entire pipeline (Challenge Pf.ipynb) of a machine learning model: Data ingestion, preprocessing, feature engineering, model training, hyperparameter tuning, model selection, and storage for deployment.

# Developing-a-Machine-learning-API-using-FastAPI

An API is generated so that the developed model can be integrated and its deployment is as simple as possible.

# Containerizing the Model using Docker

Finally, we package the model using Docker. This will help us share and scale the model.

## Run

1. Clone the project
   * `git clone git@github.com:ashmibanerjee/fastapi-backend.git`
   * `cd fastapi-backend`
2. Create virtual environment
   * `virtualenv venv`
   * `source venv/bin/activate`
3. Install dependencies 
   * `pip3 install -r requirements.txt`
4. Run the server
   * `python3 app/server.py`
5. Server should be running at `http://127.0.0.1:8000/docs`

1. With terminal navigate to the root of this repository
--------------------------------------------------------

2. Build docker image
---------------------
.. code-block::

    docker build -t image_name .

3. Run container
----------------
.. code-block::

    docker run --name container_name -p 8000:8000 image_name

4. Output will contain
----------------------
INFO:     Uvicorn running on http://0.0.0.0:8000
