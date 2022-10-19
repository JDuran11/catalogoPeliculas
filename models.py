import json

class Pelicula:
    
    def __init__(self, nombre, genero, director):
        self._nombre = nombre
        self._genero = genero
        self._director = director
        
    #Getter
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def genero(self):
        return self._genero
    
    @property
    def director(self):
        return self._director

class Catalogo():
    
    archivo = 'peliculas.json'
    
    @classmethod
    def agregarPeliculas(cls, dic):
        with open(cls.archivo, 'r') as file:
            data = json.load(file)
        
        with open(cls.archivo, 'w') as file:
            data.append(dic)
            json.dump(data, file)
        
    
    @classmethod
    def eliminarCatalogo(cls):
        with open(cls.archivo, 'w') as file:
            json.dump([], file)
    
    

    @classmethod
    def recuperarCatalogo(cls):
        with open(cls.archivo) as file:
            data = json.load(file)
        return data



