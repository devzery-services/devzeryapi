import json
from flask import Flask, request, jsonify
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Uncomment to get log file and uncomment the other logging lines in the code

# logging.basicConfig(filename='api.log', level=logging.INFO,
#                     format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

@app.route('/api', methods=['POST'])
def api():
    try:
    # Log the request headers
        headers = dict(request.headers)

        print("######## Headers #########")
        # logging.info(f"\n######## Headers #########\n {json.dumps(headers, indent=4)} \n\n")
        print(json.dumps(headers, indent=4))
        data = request.json
        print("######## Body #########")
        # logging.info(f"\n######## Body #########\n {json.dumps(data, indent=4)} \n\n")
        print(json.dumps(data, indent=4))

        return jsonify({"message":"success"})

    except Exception as e:
        return jsonify({"message": f"{e}"}), 400

@app.route('/', methods=['HEAD'])
def handle_head_request():
    # Handle HEAD request (e.g., return headers without body)
    return '', 200
