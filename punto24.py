class Pila():

    def __init__(self):
        self.__elements = []
    def push(self, dato):
        self.__elements.append(dato)
    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato
    def size(self):
        return len(self.__elements)
    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
        
pilaMCU = Pila()

pilaMCU.push({'Nombre': 'Rocket Raccoon', 'Peliculas': 5})
pilaMCU.push({'Nombre': 'Black Widow', 'Peliculas': 6})
pilaMCU.push({'Nombre': 'Groot', 'Peliculas': 4})

inicialesPersonajes = ['C','D','G']

#PUNTO A

def posicionRocketRaccoonYGroot(pila):
    posicion_Rocket =None
    posicion_Groot =None
    pila_auxiliar =Pila()

    while pila.size()>0:
        personaje = pila.pop()
        if personaje['Nombre'] == 'Rocket Raccoon':
            posicion_Rocket = pila.size()+1
        if personaje['Nombre'] == 'Groot':
            posicion_Groot = pila.size()+1 
        pila_auxiliar.push(personaje)
    while pila_auxiliar.size()>0:
        pila.push(pila_auxiliar.pop())
    return posicion_Rocket, posicion_Groot

#PUNTO B
def masDeCincoPeliculas(pila):
    personajes=[]
    while pila.size()>0:
        personaje = pila.pop()
        if personaje['Peliculas']>5:
            personajes.append((personaje['Nombre'], personaje['Peliculas']))
    return personajes

#PUNTO C
def pelisViudaNegra(pila):
    pila_auxiliar =Pila()
    contPeliculas =0

    while pila.size()>0:
        personaje = pila.pop()
        pila_auxiliar.push(personaje)
        if personaje['Nombre'] =="Black Widow":
            contPeliculas = personaje['Peliculas']     
    while pila_auxiliar.size()>0:
        pila.push(pila_auxiliar.pop()) 
    return contPeliculas

contPeliculas = pelisViudaNegra(pilaMCU)
print('Peliculas de la Viuda Negra', contPeliculas)


#PUNTO D
def inicialesBuscados(pila):
    pila_auxiliar = Pila()
    inicialesPersonajes = []

    while pila.size()>0:
        personaje = pila.pop()
        pila_auxiliar.push(personaje)
        nombre = personaje['Nombre']
        if nombre.startswith('C') or nombre.startswith('D') or nombre.startswith('G'):
            inicialesPersonajes.append(personaje)
    while pila_auxiliar.size()>0:
        pila.push(pila_auxiliar.pop())
    return inicialesPersonajes

iniciales = inicialesBuscados(pilaMCU)
print('Nombres de personajes que empiezan con C,D Y G:')
for personaje in iniciales:
    print(personaje['Nombre'])


#Listado posicion punto A
posicion_Rocket, posicion_Groot = posicionRocketRaccoonYGroot(pilaMCU)
print('La posicion de Rocket Raccoon es: ',posicion_Rocket,'y la de Groot es: ', posicion_Groot)

#Listado personajes punto B
PersonajesMasDeCincoPeliculas = masDeCincoPeliculas(pilaMCU)
print('Nombre de personajes que participaron en mas de 5 peliculas:')
for personaje, peliculas in PersonajesMasDeCincoPeliculas:
    print(personaje,'cantidad de peliculas: ', peliculas)
