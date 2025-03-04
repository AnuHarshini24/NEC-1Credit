from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({"name": "Anu Harshini"})

@app.route('/register_number', methods=['GET'])
def get_register_number():
    return jsonify({"register_number": "22it002"})

@app.route('/department', methods=['GET'])
def get_department():
    return jsonify({"department": "Information Technology"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
