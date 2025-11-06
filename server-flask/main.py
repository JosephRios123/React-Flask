from flask import Flask
from flask-cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api/users')
def get_users():
    return {
        'users': ['Jose', 'Nelida', 'Carlos']
    }

@app.route('/api/fruits')
def get_users():
    return ['Aguacate', 'Pera', 'Manzana']

if __name__ == '__main__':
    app.run(debug=True, port=5050) # by default, Flask runs on port 5000