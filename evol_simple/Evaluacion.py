"""
Este modulo contiene los metodos necesarios para la evaluación de la adaptación de cada individuo
o solución posible a nuestro problema, indicando cómo de óptima se puede considerar la
respuesta. Esto permite comparar entre posibles soluciones para encontrar cuál será la
más adecuada al problema.

@author: bbaruque
"""

import numpy as np

from deap import base

import DatosMochila as dm
import ConfiguracionSolucion

#%% Funcion de evaluacion
# A partir de un individuo pasado como parametro, permite calcular la adaptacion de dicho individuo
def evalKnapsack(individual):

    value = 0.0
    weight = 0.0
    
    # Producto vectorial de un individuo (boolean) por los datos (float)
    # Multiplica cada bit del individuo por el valor correspondiente en el vector de datos
    # y finalmente hace la suma de todos
    value = np.dot(individual,dm.values)
    weight = np.dot(individual,dm.weights) # Mismo cáculo para el vector de pesos

#    print("value: ", value)
#    print("weight: ", weight)

    # Se penaliza en caso de que el peso de la mochila exceda el maximo
    diff = dm.knapsackMax - weight
    if(diff < 0):
    	value = value + (diff * 10) # OJO: tened en cuenta que diff es negativo, por lo que en realidad está RESTANDO

    return value,

#%% Se comprueba la asignacion de fitness:
# Esta parte solo se incluye como comprobacion de la función evalKnapsack
# No es necesario incluirlo en la evaluacion

def prueba():

    #Herramienta para guardar la configuracion de la poblacion
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
    print (ind)
    print (ind.fitness.valid) # False

    ind.fitness.values = evalKnapsack(ind)

    # Se imprime el individuo DESPUES de evaluar
    print (ind.fitness.valid) # True
    print (ind.fitness)

if __name__ == "__main__":
    prueba()
