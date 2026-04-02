
import streamlit as st
import requests

API_URL = "https://players-api-pal0.onrender.com"

st.title("Players Frontend")
st.write("This frontend connects to my Players API.")

st.subheader("All Players")

if st.button("Load Players"):
    response = requests.get(f"{API_URL}/players")
    if response.status_code == 200:
        players = response.json()
        for player in players:
            st.write(f"{player['id']}: {player['name']} - {player['position']} - {player['team']} - Age {player['age']}")
    else:
        st.error("Failed to load players")

st.subheader("Add a New Player")

name = st.text_input("Name")
position = st.text_input("Position")
team = st.text_input("Team")
age = st.number_input("Age", min_value=1, max_value=100, step=1)

if st.button("Add Player"):
    new_player = {
        "name": name,
        "position": position,
        "team": team,
        "age": age
    }
    response = requests.post(f"{API_URL}/players", json=new_player)
    if response.status_code == 201:
        st.success("Player added successfully")
        st.json(response.json())
    else:
        st.error("Failed to add player")
