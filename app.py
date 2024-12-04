from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello from REST API"})

if __name__ == '__main__':
    app.run(debug=True)
