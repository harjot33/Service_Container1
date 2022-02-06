from queue import Empty
from flask import Flask, jsonify,render_template, request, redirect, url_for, session, logging
import os, requests
import datetime

app = Flask(__name__)

@app.route('/definition',methods=['POST'])
def sendword():
    if request.method == 'POST':
        content = request.get_json(force=True)
        word = content['word']
        if word is None or not word:
            response = {"word": "nil",
            "error": "Invalid JSON input."}
            return response
        else:
            word = word.strip().lower()
            content['word'] = word
            res = requests.post('http://host.docker.internal:5001/secondcontainer', json=content)
            if res.ok:
                response = res.json()
                return response

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5000')
    app.run(debug=True, port=server_port, host='0.0.0.0')