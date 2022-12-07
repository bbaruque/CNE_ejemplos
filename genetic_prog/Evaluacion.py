
import math
#import networkx as nx
#from networkx.drawing.nx_agraph import graphviz_layout

from deap import base, gp

import DatosFuncion as datos
import ConfiguracionProblema

#%% Funcion de evaluacion
# A partir de un individuo pasado como parametro, permite calcular la adaptacion de dicho individuo
#
# Evaluation function
# From an individual passed as a parameter, it allows to calculate the adaptation of this individual.
def eval_ecuacion(toolbox, individual):
    
#    tree = gp.PrimitiveTree(individual)
#    print(str(tree))
    
    # Se convierte el arbol de expresión en una función python ejecutable
    # The expression tree is converted into an executable python function.
    func = toolbox.compile(expr=individual)

    # Se calcula el error cuadrático medio (MSE) que comete la función al evaluarse sobre los diferentes datos.
    # The mean squared error (MSE) that the function commits when evaluated on the different data is calculated.
    
    # Estos son los datos CONOCIDOS
    # En este caso, se obtienen de una función, pero es probable que se tengan que leer de un fichero
    #
    # This is the KNOWN data
    # In this case, it is obtained from a function, but it is likely to have to be read from a file.
    entradas, salidas = datos.f_cuarta()
    
    # Se acumula el error (la diferencia) que se comete en la predicción de cada dato: 'x' es el dato facilitado, 'y' el dato esperado (target)
    # The error (the difference) made in the prediction of each datum is accumulated: 'x' is the given datum, 'y' is the expected (target) datum.
    sqerrors = []
    for x, y in zip(entradas,salidas):
        sqerrors.append((func(x) - y)**2) # Cuadrado del error en cada ejemplo # Square of Error in each example
    
    print('Error para cada instancia/caso del problema: ',sqerrors)

    # Se calcula la MEDIA de los errores cometidos
    # The AVERAGE of the errors made is calculated.
    return (math.fsum(sqerrors) / len(entradas)),    

#%% Funcion que permite dibujar el individuo pasado por parametro como un arbol (en lugar de una expresión lineal)
#
# Function that allows to draw the individual passed by parameter as a tree (instead of a linear expression)
#def plotExpressionTree(toolbox, individual):
#    
#    nodes, edges, labels = gp.graph(individual)
#
#    g = nx.Graph()
#    g.add_nodes_from(nodes)
#    g.add_edges_from(edges)
#    pos = graphviz_layout(g, prog="dot")
#
#    nx.draw_networkx_nodes(g, pos)
#    nx.draw_networkx_edges(g, pos)
#    nx.draw_networkx_labels(g, pos, labels)

#%% Se comprueba la asignacion de fitness:
# Esta parte solo se incluye como comprobacion de la función. No es necesario incluirlo en la evaluacion.
#
# Fitness allocation is checked:
# This part is only included as a function check. It is not necessary to include it in the evaluation.
def prueba():

    # Herramienta para guardar la configuracion de la poblacion
    # Toolbox to save the population settings
    toolbox = base.Toolbox()

    ConfiguracionProblema.configura_poblacion(toolbox)

    # Se instancia un individuo (aleatorio)
    # One individual (random) is instantiated
    ind = toolbox.individual()
    
    ### Se aconseja al alumno probar con varios individuos en diferentes condiciones de optimalidad para comprobar si la función está bien definida en todo el espacio de búsqueda.    

    ### The student is advised to test with several individuals under different optimality conditions to check if the function is well defined over the whole search space.    

    # Se imprime el individuo ANTES de evaluar
    # Individual is printed BEFORE evaluating
    tree = gp.PrimitiveTree(ind)
    print (tree)
    print (ind.fitness.valid)  # False

    ind.fitness.values = eval_ecuacion(toolbox, ind)

    # Se imprime el individuo DESPUES de evaluar
    # Individual is printed AFTER evaluating
    print ('Error Medio (Error del Individuo): ')
    print (ind.fitness.valid)    # True
    print (ind.fitness)

if __name__ == "__main__":
    prueba()
