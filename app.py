import streamlit as st
import requests

# API Base URL
BASE_URL = "https://nba-stats-db.herokuapp.com/api"

# Function to fetch data from API
def fetch_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Streamlit App
st.title("NBA Stats App")
st.image('./Basketball.png', use_column_width=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a stat to view",
    ["Player Season Stats by Name", "All Players by Season", "Top Scorers by Season", 
     "Top Scorers in the Playoffs", "Top Assists by Season", "Top Assists in the Playoffs", 
     "Top Rebounders by Season", "Player Shot Chart Data"]
)

if option == "Player Season Stats by Name":
    st.header("Player Season Stats by Name")
    player_name = st.text_input("Enter player name:")
    if player_name:
        data = fetch_data(f"{BASE_URL}/playerdata/name/{player_name}")
        if data:
            st.write(data)

elif option == "All Players by Season":
    st.header("All Players by Season")
    season = st.text_input("Enter season (e.g., 2023):")
    if season:
        data = fetch_data(f"{BASE_URL}/playerdata/season/{season}")
        if data:
            st.write(data)

elif option == "Top Scorers by Season":
    st.header("Top Scorers by Season (Total Points)")
    season = st.text_input("Enter season (e.g., 2011):")
    if season:
        data = fetch_data(f"{BASE_URL}/playerdata/topscorers/total/season/{season}")
        if data:
            st.write(data)

elif option == "Top Scorers in the Playoffs":
    st.header("Top Scorers in the Playoffs by Season (Total Points)")
    season = st.text_input("Enter season (e.g., 2011):")
    if season:
        data = fetch_data(f"{BASE_URL}/playerdata/topscorers/playoffs/{season}")
        if data:
            st.write(data)

elif option == "Top Assists by Season":
    st.header("Top Assists by Season (Total Assists)")
    season = st.text_input("Enter season (e.g., 2011):")
    if season:
        data = fetch_data(f"{BASE_URL}/top_assists/totals/{season}")
        if data:
            st.write(data)

elif option == "Top Assists in the Playoffs":
    st.header("Top Assists in the Playoffs by Season (Total Assists)")
    season = st.text_input("Enter season (e.g., 2012):")
    if season:
        data = fetch_data(f"{BASE_URL}/top_assists/playoffs/{season}")
        if data:
            st.write(data)

elif option == "Top Rebounders by Season":
    st.header("Top Rebounders by Season (Total Rebounds)")
    season = st.text_input("Enter season (e.g., 2023):")
    if season:
        data = fetch_data(f"{BASE_URL}/top_rebounds/totals/{season}")
        if data:
            st.write(data)

elif option == "Player Shot Chart Data":
    st.header("Player Shot Chart Data (Season & Playoffs)")
    player_name = st.text_input("Enter player name:")
    season = st.text_input("Enter season (e.g., 2023):")
    if player_name and season:
        data = fetch_data(f"{BASE_URL}/shot_chart_data/{player_name}/{season}")
        if data:
            st.write(data)
