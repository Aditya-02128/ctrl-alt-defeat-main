from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/receive_text": {"origins": "*"}})


@app.route('/receive_text', methods=['POST', 'OPTIONS'])
def receive_text():
    if request.method == 'OPTIONS':
        # Respond to the preflight request
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    data = request.get_json()
    received_text = data.get('text')
    print(received_text)
    # Process the received text as needed
    # ...
    #txtcmd=["python","run_script.py",received_text]
    #subprocess.run(txtcmd, stdout=subprocess.PIPE, text=True)
    return jsonify({'message': data})
    print(received_text)

'''@app.route('/get_video', methods=['GET', 'OPTIONS'])
def get_video():
    if request.method == 'OPTIONS':
        # Respond to the preflight request
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    video_path = './final_video.mp4'
    return send_file(video_path, mimetype='video/mp4')
    #return jsonify({'message': received_text})'''

if __name__ == '__main__':
    app.run(debug=True)
