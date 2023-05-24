class Pila():
    
    def __init__(self):
        self.__elements = []
    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False
    def push(self, value):
        self.__elements.append(value)
    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato
    def size(self):
        return len(self.__elements)
    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
    def __iter__(self):
        return iter(self.__elements)


class peliculas():

    def __init__(self, titulo, estudio, anio):
        self.titulo = titulo
        self.estudio = estudio
        self.anio = anio
pila_peliculas = Pila()
pila_peliculas.push(peliculas("Iron Man", "Marvel", 2014))
pila_peliculas.push(peliculas("Guardianes de la Galaxia", "Marvel", 2018))
pila_peliculas.push(peliculas("Capitan America", "Marvel", 2020))
pila_peliculas.push(peliculas("Thor", "Marvel", 2019))
pila_peliculas.push(peliculas("Avengers", "Marvel", 2016))

def mostrarXAnio(anio, pila):
    for pelicula in pila:
        if pelicula.anio == anio:
            print(pelicula.titulo)
def contarXAnio(anio, pila):
    contador = 0
    for pelicula in pila:
        if pelicula.anio ==anio:
            contador +=1
    return contador
def mostrarMarvelXAnio(anio, pila):
    for pelicula in pila:
        if pelicula.anio == anio and pelicula.estudio == "Marvel":
            print(pelicula.titulo)

print("Peliculas de 2014:")
mostrarXAnio(2014, pila_peliculas)
cantidadPeliculasDe2018 = contarXAnio(2018, pila_peliculas)
print(f"Cantidad de peliculas de 2018: {cantidadPeliculasDe2018}")
print("Peliculas de Marvel de 2016:")
mostrarMarvelXAnio(2016, pila_peliculas)
