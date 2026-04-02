
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
st.subheader("Get Player by ID")

player_id = st.number_input("Enter Player ID", min_value=1, step=1, key="get_id")

if st.button("Get Player"):
    response = requests.get(f"{API_URL}/players/{player_id}")
    if response.status_code == 200:
        player = response.json()
        st.success("Player found")
        st.json(player)
    else:
        st.error("Player not found")
        st.subheader("Delete Player")

delete_id = st.number_input("Player ID to delete", min_value=1, step=1, key="delete_id")

if st.button("Delete Player"):
    response = requests.delete(f"{API_URL}/players/{delete_id}")
    if response.status_code == 200:
        st.success("Player deleted")
        st.json(response.json())
    else:
        st.error("Failed to delete player")
        st.subheader("Update Player")

update_id = st.number_input("Player ID to update", min_value=1, step=1, key="update_id")

new_name = st.text_input("New Name", key="u_name")
new_position = st.text_input("New Position", key="u_position")
new_team = st.text_input("New Team", key="u_team")
new_age = st.number_input("New Age", min_value=1, max_value=100, step=1, key="u_age")

if st.button("Update Player"):
    updated_player = {
        "name": new_name,
        "position": new_position,
        "team": new_team,
        "age": new_age
    }
    response = requests.put(f"{API_URL}/players/{update_id}", json=updated_player)
    if response.status_code == 200:
        st.success("Player updated")
        st.json(response.json())
    else:
        st.error("Failed to update player")
