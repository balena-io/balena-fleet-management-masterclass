from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the balena Fleet Management Masterclass"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
