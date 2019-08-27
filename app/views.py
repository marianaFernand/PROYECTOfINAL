from app import app
from flask import render_template, request ,redirect, url_for, flash
from app.forms import BuscaTodos
import csv
import json

@app.route('/', methods= ['GET','POST'])
def index():
    form = BuscaTodos()
    if request.method == 'POST':
        # Esto es cuando recibes un POST
        #    Falta escribir la cadena de búsqueda en algún sitio
        #    Pero yo creo que aquí nunca recibes un post, que lo recibes en la siguiente página (indice)
        return redirect (ulr_for('indice'))
    else:
        # Aquí cuando recibes un get normal, solo hay que mostrar la página
        #    La ruta a la plantilla la tienes que cambiar
        return render_template('index.html', form=form)


@app.route('/indice', methods= ['GET','POST'])
def indice():
    pelicula = None
    if request.method == 'GET':
        # Esto es cuando te metes en la página normal// cuando "volvemos"
        pass # Esto no hace nada, lo pongo para que no me de error (luego lo cambiamos)
    else:
        # Esto es cuando te mandan un POST (cuando te llaman desde la página principal)
        data_lista= """{"Search":[{"Title":"Promedio Rojo","Year":"2004","imdbID":"tt0415219","Type":"movie","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4OTAyMzA2M15BMl5BanBnXkFtZTcwNjE3MTAzMQ@@._V1_SX300.jpg"},{"Title":"Rojo","Year":"2018","imdbID":"tt8956390","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BN2RkNDAwZDgtZDBhNC00ZTVkLTgzMWItMzhiOTJiMGM3Yzk5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"},{"Title":"Rojo sangre","Year":"2004","imdbID":"tt0385993","Type":"movie","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNmFkYTI2NWMtZGE4ZS00M2UxLWI5ZTMtZTNkZjcwNzk1MTQyXkEyXkFqcGdeQXVyODcwNzMxNg@@._V1_SX300.jpg"},{"Title":"El cielo rojo","Year":"2008","imdbID":"tt1280502","Type":"movie","Poster":"N/A"},{"Title":"Rojo y negro","Year":"1942","imdbID":"tt0035264","Type":"movie","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMzAwNmQ2ODEtOWZiNC00YTZiLWJjZDItYzFiZDhjMjI1NDQ3XkEyXkFqcGdeQXVyNjUyMTgxNjA@._V1_SX300.jpg"},{"Title":"Rojo, la película","Year":"2006","imdbID":"tt0805600","Type":"movie","Poster":"N/A"},{"Title":"Rojo","Year":"1966","imdbID":"tt0062211","Type":"movie","Poster":"N/A"},{"Title":"Crónica sentimental en rojo","Year":"1986","imdbID":"tt0088972","Type":"movie","Poster":"https://m.media-amazon.com/images/M/MV5BMzI0NWVmMjQtMmY3MS00ODNjLWJjMTgtNmRhMWU1YmQ4ODMzXkEyXkFqcGdeQXVyMTAxMDQ0ODk@._V1_SX300.jpg"},{"Title":"Mar rojo","Year":"2005","imdbID":"tt0445084","Type":"movie","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNTA5MzY1Nzc3Nl5BMl5BanBnXkFtZTcwODA1NDk2MQ@@._V1_SX300.jpg"},{"Title":"La Banda Del Carro Rojo","Year":"1978","imdbID":"tt0315254","Type":"movie","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNjFiM2NlODEtOGQ5OC00OGRkLWI0YzEtMDViNmQ5OWYzOTM2XkEyXkFqcGdeQXVyNDI2ODQxMw@@._V1_SX300.jpg"}],"totalResults":"104","Response":"True"}"""
        lista = json.loads(data_lista)
        pelicula = lista["Search"]

    return render_template('indice.html', peliculas = pelicula)

@app.route('/final', methods= ['GET','POST'])
def final():
    if request.method == 'GET':
        # Esto es cuando te metes en la página normal, yo creo que nunca se llamará
        pass # Esto no hace nada, lo pongo para que no me de error (luego lo cambiamos)
    else:
        # Esto es cuando te mandan un POST (cuando te llaman desde el listado con un ID de pelicula)
        pass # Esto no hace nada, lo pongo para que no me de error (luego lo cambiamos)
    return render_template('final.html')


    
