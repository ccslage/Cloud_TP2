import pandas as pd
import requests

# Read the songs data
songs = pd.read_csv('C:\\Users\\carlo\\OneDrive\\Documents\\GitHub\\Cloud\\TP2\\data\\2023_spotify_songs.csv')

# Iterate through each track_name and send a request to the server
iteration = 0
for track_name in songs['track_name']:
    print(f'Iteration: {iteration}')
    
    # Prepare the request payload
    payload = {
        'songs': [track_name]  # Sending one track at a time
    }

    # Send a POST request to the server
    response = requests.post('http://127.0.0.1:5000/recommendations', json=payload)

    # Print the response from the server
    if response.status_code == 200:
        recommended_songs = response.json().get(track_name, [])
        recommended_songs_str = ', '.join(recommended_songs) if recommended_songs else "No Recommendations"
        print(f"Request sent for track: {track_name}")
        print(f"Response received: {recommended_songs_str}")
    else:
        print(f"Request sent for track: {track_name}")
        print(f"Failed to get recommendations: {response.status_code}")
    
    iteration += 1
    print('\n')