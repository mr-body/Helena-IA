from flask import Flask, request, jsonify, render_template

from functions.genai import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/tolking')
def tolk():
    return render_template('tolk.html')

@app.route('/question/text', methods=['POST'])
def generate_response():
    data = request.get_json()
    user_input = data['text']

    # Get the last message in the conversation history
    response = question(user_input)
    property(user_input)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
