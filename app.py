from flask import Flask
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)
CORS(app, origins="https://doc.prots.kz")
@app.route('/runcode', methods=['GET', 'POST'])
@cross_origin()
def run_code():
    try:
        # Run the Python code using subprocess
        result = subprocess.check_output(['python', 'test.py'], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=("cert.pem", "key.pem"))