import json
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_issue', methods=['POST'])
def create_issue():
    data = request.get_json()
    body = data.get('body')

    # Call your Python function to create an issue
    result = make_github_issue(body)

    return jsonify({'result': result})


def make_github_issue(body):
    # Your personal access token with necessary permissions
    token = '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'

    # API endpoint for creating an issue
    url = f'https://api.github.com/repos/Onyx39/onyx39.github.io/issues'

    # Form data to be submitted (replace with your actual form data)
    data = {
        'title': 'New data',
        'body': body
    }

    # Convert data to JSON
    json_data = json.dumps(data)

    # Set headers with authorization and content type
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/json'
    }

    # Make a POST request to create an issue
    response = requests.post(url, data=json_data, headers=headers)

    # Check the response
    if response.status_code == 201:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
