import streamlit as st
from xgb_predictor import predict_play

# Streamlit app setup
st.title("NFL Coverage 4th Qtr EPA Predictor")

# Constants
lengths = ['short', 'deep'] # Why no middle? Should we use air yards instead?
locations = ['left', 'right', 'middle']
routes = ['SCREEN', 'OUT', 'IN', 'SLANT', 'GO', 'HITCH', 'CROSS', 'ANGLE', 'FLAT', 'POST', 'CORNER', 'WHEEL']

# User inputs
yardline_100 = st.number_input("Yards from endzone", min_value = 1, max_value = 99, value = 25)
quarter_seconds_remaining = st.number_input("Time Remaining in 4th Qtr (seconds)", min_value=0, max_value = 120, value=120)
#down = st.selectbox("Down", [1, 2, 3, 4])
ydstogo = st.slider("Distance to First Down (yards)", 1, 30, 1)
defenders_in_box = st.slider("Defenders in the box", 1, 11, 1)
number_of_pass_rushers = st.slider("Number of pass rushers", 1, 11, 1)
no_huddle = st.checkbox("No huddle?")
out_of_bounds = st.checkbox("Did play go out of bounds?")
pressure = st.checkbox("Was the QB pressured?")
time_to_throw = st.slider("Time to throw (seconds)", min_value = 0.5, max_value = 13.5, value = 2.67, step = 0.01)
pass_length = st.selectbox('Choose pass length:', lengths)
pass_location = st.selectbox('Choose pass location:', locations)
route = st.selectbox('Choose route completed:', routes)
# score_difference = st.number_input("Score Difference (Offense - Defense)", value=0)

# Create feature dictionary
features = {
    'yardline_100' : yardline_100,
    'quarter_seconds_remaining': quarter_seconds_remaining,
    'ydstogo': ydstogo,
    'no_huddle': no_huddle,
    'length_encoded': pass_length,
    'location_encoded': pass_location,
    'out_of_bounds': out_of_bounds,
    'defenders_in_box': defenders_in_box,
    'number_of_pass_rushers': number_of_pass_rushers,
    'time_to_throw': time_to_throw,
    'pressure_encoded': pressure,
    'route_encoded': route,
}

# Predict and display results
if st.button("Predict EPAs Per Coverage"):
    play = predict_play(features)
    output = play[['Coverage', 'predicted_EPA']].sort_values(by=['predicted_EPA'])
    st.write(f"### Predicted EPAs Based on Scenario: ")
    st.dataframe(output)
    