from flask import Flask, render_template, request
from geopy.distance import geodesic
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
