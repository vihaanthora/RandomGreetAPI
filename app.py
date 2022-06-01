from base64 import encode
from encodings import utf_8
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if(request.args.get('name')):
        name = request.args.get('name')
    else:
        return "Pass a name in the URL as /?name=John"
    if(name):
        response = requests.get("https://www.greetingsapi.com/random")
        json_data = response.json()
        greeting = f"{json_data['greeting']} {name.capitalize()}! That's the way you greet someone in {json_data['language']}."
        return greeting

if __name__ == '__main__':
    app.run(debug=True)
