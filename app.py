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
        headers_output = json.dumps(headers, indent=4)

        # Log the request body
        data = request.json
        body_output = json.dumps(data, indent=4)

        # Create a response message containing the printed headers and body
        response_message = {
            "headers": headers_output,
            "body": body_output
        }

        return jsonify(response_message)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['HEAD'])
def handle_head_request():
    # Handle HEAD request (e.g., return headers without body)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
