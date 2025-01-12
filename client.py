#----------------------------------------------------------------------------------------------------------------------------------------------
#  Project 2: DevOps and Cloud Computing
#
#  Discipline: Cloud Computing
#
#  Author: Carlos Cezar Silva Lage
#
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#  Client: API REST CLIENT
#
#  Description: Implements the IHM to get the music used as search key from user, send to MLServer and receive the list of musics recommended
#               from it end show this list to user in the web browser
#
#  Output: Shows the list of musics recommended to user in web browser
#
#----------------------------------------------------------------------------------------------------------------------------------------------
#
import requests
import os

def get_recommendations(track_names):
    # Use environment variable or default to localhost for local testing
    url = os.getenv('MLSERVICE_URL', 'http://mlserver:5000/recommendations')
    payload = {'songs': track_names}
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            recommendations = response.json()
            print("Recommendations:")
            for track, recs in recommendations.items():
                print(f"{track}: {', '.join(recs) if recs else 'No recommendations found.'}")
        else:
            print(f"Failed to get recommendations: {response.status_code}, {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    print("Enter track names (comma-separated or one per line). Type 'exit' to finish:")
    
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break
        track_names = [track.strip() for track in user_input.split(',')]
        
        if track_names:
            get_recommendations(track_names)
        else:
            print("No track names provided.")
