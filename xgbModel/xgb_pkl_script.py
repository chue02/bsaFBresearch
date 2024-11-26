import math
import pandas as pd
import os
import xgboost as xgb
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Data Acquisition and Preprocessing

# Initialize dictionaries of dataframes
data = {}
years = [18, 19, 20, 21, 22, 23]

# Load data per year

for x in years:
    data[x] = pd.read_csv('../cleanData/refined/pbp_refined_20' + str(x) + '.csv')

# Create one large dataframe containing all the data
df = pd.concat(data, ignore_index=True)

# Filter data based on 2 min drill

df = df[df['offense_personnel'] == '1 RB, 1 TE, 3 WR']
df = df[df['qtr'] == 4]
df = df[df['quarter_seconds_remaining'] <= 120]

df.dropna(subset=['epa'], inplace=True) # For some reason there is a NaN for EPA in 18385

# Encode categorical features 
le_route = LabelEncoder()
df['route_encoded'] = le_route.fit_transform(df['route'])

le_coverage = LabelEncoder()
df['coverage_encoded'] = le_coverage.fit_transform(df['defense_coverage_type'])

le_pressure = LabelEncoder()
df['pressure_encoded'] = le_pressure.fit_transform(df['was_pressure'])

le_length = LabelEncoder()
df['length_encoded'] = le_length.fit_transform(df['pass_length'])

le_location = LabelEncoder()
df['location_encoded'] = le_location.fit_transform(df['pass_location'])

# Convert the encoded columns to 'category' type
# Ensure they are encoded as integers, no idea why they're objects
df['route_encoded'] = df['route_encoded'].astype(int)
df['pressure_encoded'] = df['pressure_encoded'].astype(int)
df['length_encoded'] = df['length_encoded'].astype(int)
df['location_encoded'] = df['location_encoded'].astype(int)

# Model implementation


X = df[['yardline_100', 'quarter_seconds_remaining', 'ydstogo', 'no_huddle', 'length_encoded', 'location_encoded', 'out_of_bounds',
        'defenders_in_box', 'number_of_pass_rushers', 'time_to_throw', 'pressure_encoded', 'route_encoded', 'coverage_encoded']]

y = df[['epa']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test, = train_test_split(
    X, y, test_size=0.2, random_state=97
)

# Train XGBoost regression model to predict EPA
model = xgb.XGBRegressor(objective="reg:squarederror")
model.fit(X_train, y_train)


# Save the trained model
with open("xgbModel.pkl", "wb") as f:
    pickle.dump(model, f)