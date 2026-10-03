import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("ipl_score_prediction_model.pkl")

st.set_page_config(
    page_title="IPL First-Innings Score Prediction",
    page_icon="🏏"
)

st.title("🏏 IPL First-Innings Score Prediction")
st.write("Predict the final first-innings score using the match situation after 10 overs.")

# Teams
teams = [
    "Chennai Super Kings",
    "Delhi Daredevils",
    "Kings XI Punjab",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Rajasthan Royals",
    "Royal Challengers Bangalore",
    "Sunrisers Hyderabad",
    "Gujarat Lions",
    "Rising Pune Supergiants"
]

# Venues
venues = [
    "Barabati Stadium",
    "Brabourne Stadium",
    "Buffalo Park",
    "De Beers Diamond Oval",
    "Dr DY Patil Sports Academy",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
    "Dubai International Cricket Stadium",
    "Eden Gardens",
    "Feroz Shah Kotla",
    "Green Park",
    "Himachal Pradesh Cricket Association Stadium",
    "Holkar Cricket Stadium",
    "JSCA International Stadium Complex",
    "Kingsmead",
    "M Chinnaswamy Stadium",
    "MA Chidambaram Stadium, Chepauk",
    "Maharashtra Cricket Association Stadium",
    "Nehru Stadium",
    "New Wanderers Stadium",
    "Newlands",
    "OUTsurance Oval",
    "Punjab Cricket Association IS Bindra Stadium, Mohali",
    "Punjab Cricket Association Stadium, Mohali",
    "Rajiv Gandhi International Stadium, Uppal",
    "Sardar Patel Stadium, Motera",
    "Saurashtra Cricket Association Stadium",
    "Sawai Mansingh Stadium",
    "Shaheed Veer Narayan Singh International Stadium",
    "Sharjah Cricket Stadium",
    "Sheikh Zayed Stadium",
    "St George's Park",
    "Subrata Roy Sahara Stadium",
    "SuperSport Park",
    "Vidarbha Cricket Association Stadium, Jamtha",
    "Wankhede Stadium"
]

st.subheader("Match Information")

batting_team = st.selectbox(
    "Batting Team",
    teams
)

bowling_team = st.selectbox(
    "Bowling Team",
    teams
)

venue = st.selectbox(
    "Venue",
    venues
)

st.subheader("Match Situation After 10 Overs")

runs = st.number_input(
    "Runs after 10 overs",
    min_value=0,
    max_value=200,
    value=70
)

wickets = st.number_input(
    "Wickets lost",
    min_value=0,
    max_value=10,
    value=2
)

runs_last_5 = st.number_input(
    "Runs in last 5 overs",
    min_value=0,
    max_value=100,
    value=35
)

wickets_last_5 = st.number_input(
    "Wickets lost in last 5 overs",
    min_value=0,
    max_value=10,
    value=1
)

if st.button("🏏 Predict Final Score"):

    input_data = pd.DataFrame({
        "batting_team": [batting_team],
        "bowling_team": [bowling_team],
        "venue": [venue],
        "runs": [runs],
        "wickets": [wickets],
        "runs_last_5": [runs_last_5],
        "wickets_last_5": [wickets_last_5]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"🏏 Predicted Final Score: {round(prediction)} runs"
    )
