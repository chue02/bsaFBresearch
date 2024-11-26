import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgb_pkl_script import le_route, le_coverage, le_pressure, le_length, le_location, y
import xgboost as xgb
import streamlit as st

# Constants
coverages = ['COVER_3', 'COVER_4', 'COVER_1', 'COVER_0', 'COVER_6', 'COVER_2', '2_MAN', 'PREVENT']

# Function to load the model
def load_model():
    with open("xgbModel.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Function to encode categorical features
def encoder(features):
    features['route_encoded'] =  le_route.transform([features['route_encoded']])
    features['pressure_encoded'] = le_pressure.transform([features['pressure_encoded']])
    features['length_encoded'] = le_length.transform([features['length_encoded']])
    features['location_encoded'] =  le_location.transform([features['location_encoded']])


# Function that returns a dataframe that contains all coverage possibilities based on scenario
def addCvgs(features):
    predict_data = []

    for x in range(len(coverages)):
        new_row = {**features, 'coverage_encoded': x
        }
        predict_data.append(new_row)
    
    scenario = pd.DataFrame(predict_data)
    return scenario

def encodeColumns(scenario):
    # Ensure encoded features are typed integers, no idea why they're objects
    scenario['route_encoded'] = scenario['route_encoded'].astype(int)
    scenario['pressure_encoded'] = scenario['pressure_encoded'].astype(int)
    scenario['length_encoded'] = scenario['length_encoded'].astype(int)
    scenario['location_encoded'] = scenario['location_encoded'].astype(int)

# Function to return dataframe of predictions
def predict_play(features):
    model = load_model()  # Load the saved model
    encoder(features) # Encode categorical features
    scenario = addCvgs(features)  # Convert input to DataFrame data for all coverage possibilities
    encodeColumns(scenario) # Encode dataframe columns from objects to categories or ints
    predicted_EPA = model.predict(scenario)
    scenario['Coverage'] = coverages
    scenario['predicted_EPA'] = predicted_EPA
    return scenario

