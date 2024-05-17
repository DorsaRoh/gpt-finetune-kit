from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# set openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "test",
        'people': ['1', '2', '3']
    })

# /api/text
@app.route("/api/text", methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # model
            messages=[ # role of model and user
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        generated_text = response.choices[0].message['content'].strip()
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)
