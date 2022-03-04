from flask import Flask, jsonify, request, make_response
import argparse

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    pass

@app.route('/verify', methods=['POST'])
def verify():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=5000,
        help='Port of serving api')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
