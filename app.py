from flask import Flask, render_template, request
import json
from news_search import create_index, search_index

app = Flask(__name__)

# Assuming you have an 'all_news_data.json' file
with open('all_news_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create or open an index for the collected JSON data
create_index(data)

@app.route('/')
def index():
    # Pass the latest 10 entries to the template
    latest_entries = data[-10:][::-1]  # Reverse the order to show the latest first
    return render_template('index.html', latest_entries=latest_entries)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_index(query, data)  # Pass the 'data' parameter to search_index

    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
