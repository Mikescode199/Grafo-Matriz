import networkx as nx
import graphviz

# By Mike el depredador

def Grafo_crear():
    Grafo = nx.Graph()
    numero_nodos = int(input("Cuantos nodos tenemos: "))
    for n in range(numero_nodos):
        nodo = input("Ingresar nodo: ")
        Grafo.add_node(nodo)
        n_aristas = int(input("Ingresar numero de aristas: "))
        for a in range(n_aristas):
            arista = input("Ingresa Arista: ")
            Grafo.add_edge(nodo, arista)    

    print(len(Grafo.nodes))
    print(len(Grafo.edges))
    print(Grafo.nodes)
    print(Grafo.edges)

    f = nx.nx_agraph.to_agraph(Grafo)
    nombre_grafo = input("Nombre del Grafo: ")
    f.layout('dot')
    f.draw(nombre_grafo + ".png") 
    

Grafo_crear()
