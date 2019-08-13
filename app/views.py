from app import app
from flask import render_template, request ,redirect, url_for, flash
import csv 

ficheroPelicula = 'data/pelicula.txt'

@app.route('/', methods= ['GET','POST'])
def index():
    if request.methods == 'POST':
        Fpelicula = open(ficheroPelicula,'a+')
        registro = (request.values['comentarios'])
        #lo tomo de index? el value? o es otra cosa
        Fpelicula.write(registro)
        Fpelicula.close()
        return redirect (ulr_for('indice'))
    else:
        msg = validar (request.values)
        if msg != True:
            return render_template('/', errores = msg)

 def validar (values):
    errores = []
    if values ['comentarios']=='':
        error.append('debe introduces un titulo')
    if len(errores) == 0:
        return True
    else:
        return errores


@app.route('/indice',methods= ['GET','POST'])
def indice():
    if request.methods == 'GET':
        Fpelicula= open(ficheroPelicula,'r')
        
    ##lo traigo relleno de arriba y debo leer el titutlo para usarlo
    ##comparar los datos y enviar la elegida 

    return render_template('indice.html')

@app.route('/final')
def final():
    return render_template('final.html')


    