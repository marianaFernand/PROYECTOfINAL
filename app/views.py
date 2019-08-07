from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.router('/indice')
def indice():
    return render_template('indice.html')

@app.router('/final')
def final():
    return render_template('final.html')
    