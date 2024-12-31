from flask import Flask, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

# Load the pivoted DataFrame once when the server starts
pivoted_df = pd.read_csv('C:\\Users\\carlo\\OneDrive\\Documents\\GitHub\\Cloud\\TP2\\rules_search_table.csv')

# Function to find consequents
def find_consequents(track_name):
    escaped_track_name = re.escape(track_name)
    
    # Filter the pivoted_df where 'antecedents' contains the given track_name
    results = pivoted_df[pivoted_df['antecedents'].str.contains(escaped_track_name, na=False)]
    
    # Convert frozensets to a string representation for easier printing
    if not results.empty:
        # Extract recommendations, remove the frozenset format, and return as a list
        return [item for sublist in results['consequents'] for item in eval(sublist)]  # Flatten the list

    return []

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json  # Expecting JSON payload
    songs = data.get('songs', [])
    
    recommendations = {}
    for song in songs:
        recommendations[song] = find_consequents(song)
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')