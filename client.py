import sys
import requests

def get_recommendations(track_names):
    url = 'http://mlserver:5000/recommendations'  # Use container name for resolving IP
    payload = {'songs': track_names}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        recommendations = response.json()
        print("Recommendations:")
        for track, recs in recommendations.items():
            print(f"{track}: {', '.join(recs) if recs else 'No recommendations found.'}")
    else:
        print(f"Failed to get recommendations: {response.status_code}, {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide track names as command line arguments.")
        sys.exit(1)

    track_names = [track.strip() for track in sys.argv[1].split(',')]
    
    get_recommendations(track_names)