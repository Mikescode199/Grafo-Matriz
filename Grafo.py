class Nodo():

    def __init__(self, vertice : str):
        self.vertice = vertice
        self.aristas = []

    def agregar_arista(self):
        numero_vertices = int(input("Número de aristas del Vertice: "))
        for i in range(numero_vertices):
            vertice = input("Ingresa vertice: ")
            self.aristas.append(vertice)
        

def Grafo():
    grafo = []
    numero_nodos = int(input("Cuantos nodos tenemos: "))
    for n in range(numero_nodos):
        nodo = input("Ingresar nodo: ")
        nodo_nuevo = Nodo(nodo)
        nodo_nuevo.agregar_arista()
        grafo.append(nodo_nuevo.vertice)
        grafo.append(nodo_nuevo.aristas)

    for g in grafo:
        print(g)

Grafo()
