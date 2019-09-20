# Puedes consultar la pagina en
    [PELICULEITOR.COM](http://3.15.234.177/)

# Instalación en local
## Instalación de dependencias

    Ejecutar pip install -r requirements.txt

## Crear documento "config.py" con los siguientes datos:
    
    SECRET_KEY= 'TU CLAVE'
    
    ALL_FILM = 'http://www.omdbapi.com/?apikey={}&s={}&v=1&type=movie&page={}'
    
    CHECK_FILM = 'http://www.omdbapi.com/?apikey={}&v=1&type=movie&i={}&plot=full'

## Lanzar aplicación

    Crear variable de entorno FLASK_APP = run.py
        En windows "set FLASK_APP=run.py"
        En mac/Linux "export FLASK_APP=run.py"

    Lanzar aplicación en desarrollo
        "flask run"


