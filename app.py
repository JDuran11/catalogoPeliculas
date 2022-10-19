from flask import Flask, render_template, request
from models import *
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
   
   #Ingresar datos
   if request.method == 'POST':
   
      nombre = request.form.get('nombre')
      genero = request.form.get('genero')
      director = request.form.get('director')
      
      pelicula = Pelicula(nombre, genero, director)
      
      newPelicula = {
         "nombre": pelicula.nombre,
         "genero": pelicula.genero,
         "director": pelicula.director
      } 
      
      Catalogo.agregarPeliculas(newPelicula)

   #Mostrar datos
   datos = Catalogo.recuperarCatalogo()  

   
   return render_template('index.html', datos = datos) 

@app.route('/borrar')
def borrar():
   Catalogo.eliminarCatalogo()
   
   return redirect(url_for('index'))