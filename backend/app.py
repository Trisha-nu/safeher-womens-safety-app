from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sos')
def sos():
    return jsonify({
        "message": "SOS Alert Sent Successfully!"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)