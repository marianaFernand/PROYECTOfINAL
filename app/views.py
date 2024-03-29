from app import app
import config
from flask import render_template, request ,redirect, url_for, flash
from app.forms import BuscaTodos
import csv
import json
import requests

@app.route('/', methods= ['GET'])
def index():
    form = BuscaTodos(pagina = 1)
    errorMsg = request.args.get('errorMsg', '')
    return render_template('index.html', form=form, errorMsg=errorMsg)

    
@app.route('/indice', methods= ['GET','POST'])
def indice():
    if request.method == 'POST':
        paginaActual = int (request.form["pagina"])
        busquedActual = request.form["titulo"]
        
        URL = config.ALL_FILM.format(config.SECRET_KEY, busquedActual ,paginaActual )
        data_lista = requests.get(URL).text
        lista = json.loads(data_lista)
        

        if lista['Response'] != 'True':
            return redirect ( './?errorMsg=No+hay+resultados+de+b%C3%BAsqueda')

        peliculas = lista["Search"]
        totalPeliculas = int (lista["totalResults"])
        
        
        totalPaginas = totalPeliculas // 10
        if totalPeliculas % 10 != 0:
            totalPaginas = totalPaginas + 1
    
        primeraPagina = paginaActual-2 
        ultimaPagina = paginaActual+2 
        if ultimaPagina <5:
            ultimaPagina = 5
        
        
        if ultimaPagina > totalPaginas:
            ultimaPagina=totalPaginas
            primeraPagina=totalPaginas-4
        
        if primeraPagina <1:
            primeraPagina=1
        
                
        pagina = 1
        return render_template('indice.html',
                           peliculas = peliculas,
                           paginaActual = paginaActual,
                           busquedActual = busquedActual,
                           totalPaginas = totalPaginas,
                           pagina = pagina,
                           primeraPagina = primeraPagina,
                           ultimaPagina = ultimaPagina
                           )
                           
    return redirect (url_for('index'))

@app.route('/final', methods= ['GET','POST'])
def final():
    if request.method == 'POST':
        peliculaActual = request.form["btnselected"]
        paginaActual = request.form["pagina"]
        busquedActual = request.form["titulo"]

        URL = config.CHECK_FILM.format(config.SECRET_KEY, peliculaActual)
        data_peli = requests.get(URL).text
        peli = json.loads(data_peli)

        return render_template('final.html',
                            pelicula = peli,
                            paginaActual = paginaActual,
                            busquedActual = busquedActual)
    return redirect ( url_for('index'))


    
