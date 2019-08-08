from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def indice():
    return render_template('indice.html')

@app.route('/')
def final():
    return render_template('final.html')
    