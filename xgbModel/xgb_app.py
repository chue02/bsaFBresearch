import streamlit as st
from xgb_predictor import predict_play

# Streamlit app setup
st.title("NFL Coverage 4th Qtr EPA Predictor")

# Constants
LENGTHS = ['short', 'deep'] # Why no middle? Should we use air yards instead?
LOCATIONS = ['left', 'right', 'middle']
ROUTES = ['SCREEN', 'OUT', 'IN', 'SLANT', 'GO', 'HITCH', 'CROSS', 'ANGLE', 'FLAT', 'POST', 'CORNER', 'WHEEL']

# User inputs
score_diff = st.slider("Points down by", min_value = 0, max_value = 8, value = 4)
yardline_100 = st.number_input("Yards till Opponent's Endzone", min_value = 1, max_value = 99, value = 75)
quarter_seconds_remaining = st.number_input("Time Remaining in 4th Qtr (seconds)", min_value=0, max_value = 120, value=120)

huddle_col, timeouts_col, down_col = st.columns(3)
with huddle_col:
    no_huddle = st.toggle("No huddle?", value = False)
with timeouts_col:
    timeouts = st.radio("Timeouts left", [0, 1, 2, 3], index = 3)
with down_col:
    down = st.radio("Down", [1, 2, 3, 4], index = 0)
    
ydstogo = st.number_input("Distance to First Down (yards)", 1, 30, value = 10, step = 1)

defenders_in_box = st.slider("Defenders in the box", 0, 9, value = 5, step = 1)
number_of_pass_rushers = st.slider("Number of pass rushers", 0, 8, value = 4, step = 1)
time_to_throw = st.slider("Time to throw (seconds)", min_value = 0.5, max_value = 13.5, value = 2.67, step = 0.01)

oob_col, press_col = st.columns(2)
with oob_col:
    out_of_bounds = st.checkbox("Did play go out of bounds?", value = False)
with press_col:
    pressure = st.checkbox("Was the QB pressured?", value = False)

# TODO: For the following two features, we may not want to consider them if we're selecting multiple routes
# Moreover, we may want to just drop them in general, particularly 'Pass length'
pass_length = st.selectbox('Pass length', LENGTHS) 
pass_location = st.selectbox('Pass location', LOCATIONS)

# TODO: Update app such that it'll let a user select multiple routes
# SO turn 'route_selected' from a scalar to a list with 'routes_selected'
# and adjust dictionary to reflect this change
route_selected = st.selectbox('Route targeted', ROUTES)

# Create feature dictionary
features = {
    'score_differential_post': score_diff * -1, 
    'yardline_100' : yardline_100,
    'quarter_seconds_remaining': quarter_seconds_remaining,
    'down': down,
    'ydstogo': ydstogo,
    'posteam_timeouts_remaining': timeouts,
    'no_huddle': no_huddle,
    'length_encoded': pass_length,
    'location_encoded': pass_location,
    'out_of_bounds': out_of_bounds,
    'defenders_in_box': defenders_in_box,
    'number_of_pass_rushers': number_of_pass_rushers,
    'time_to_throw': time_to_throw,
    'pressure_encoded': pressure,
    'route_encoded': route_selected
}

# Predict and display results
if st.button("Predict EPAs per Coverage"):
    play = predict_play(features)
    output = play[['Coverage', 'predicted_EPA']].sort_values(by=['predicted_EPA'])
    st.write(f"### Predicted EPAs Based on Scenario: ")
    st.dataframe(output, hide_index=True)

    