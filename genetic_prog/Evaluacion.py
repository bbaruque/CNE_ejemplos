
import math
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

from deap import base, gp

import DatosFuncion as datos
import ConfiguracionProblema

#%% Funcion de evaluacion
# A partir de un individuo pasado como parametro, permite calcular la adaptacion de dicho individuo
def evalEcuacion(toolbox, individual):
    
#    tree = gp.PrimitiveTree(individual)
#    print(str(tree))
    
    # Se convierte el arbol de expresión en una función python ejecutable
    func = toolbox.compile(expr=individual)
    # Se calcula el error cuadrático medio que comete la función
    # al evaluarse sobre los diferentes datos
    entradas, salidas = datos.fCuarta()
    
    sqerrors = []
    for x,y in zip(entradas,salidas):
        sqerrors.append((func(x) - y)**2)
        
    return (math.fsum(sqerrors) / len(entradas)),    

#%% Funcion que permite dibujar el individuo pasado por parametro
# como un arbol (en lugar de una expresión lineal)
def plotExpressionTree(toolbox, individual):
    
    nodes, edges, labels = gp.graph(individual)

    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    pos = graphviz_layout(g, prog="dot")

    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos, labels)
    plt.show()

#%% Se comprueba la asignacion de fitness:
# Esta parte solo se incluye como comprobacion de la función
# No es necesario incluirlo en la evaluacion

def prueba():

    '''Herramienta para guardar la configuracion de la poblacion'''
    toolbox = base.Toolbox()

    ConfiguracionProblema.configuraPoblacion(toolbox)

    # Se instancia un individuo (aleatorio)
    ind = toolbox.individual()
    
    '''
    Se aconseja al alumno probar con varios individuos en diferentes condiciones
    de optimalidad para comprobar si la función está bien definida en todo el 
    espacio de búsqueda.    
    '''
    # Se imprime el individuo ANTES de evaluar
    tree = gp.PrimitiveTree(ind)
    print (tree)
    print (ind.fitness.valid)  # False

    ind.fitness.values = evalEcuacion(toolbox, ind)

    # Se imprime el individuo DESPUES de evaluar
    print (ind.fitness.valid)    # True
    print (ind.fitness)

if __name__ == "__main__":
    prueba()
