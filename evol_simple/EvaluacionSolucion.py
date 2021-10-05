"""
Este modulo contiene los metodos necesarios para la evaluación de la adaptación de cada individuo o solución posible a nuestro problema, indicando cómo de óptima se puede considerar la respuesta. 
Esto permite comparar entre posibles soluciones para encontrar cuál será la más adecuada al problema.

---

This module contains the necessary methods for the evaluation of the adaptation of each individual or possible solution to our problem, indicating how optimal the response can be considered. 

This allows us to compare between possible solutions to find the one that will be the most best suited to the problem.

@author: bbaruque
"""

import numpy as np

from deap import base

import evol_simple.DatosMochila as dm
import evol_simple.ConfiguracionSolucion

#%% Funcion de evaluacion
# A partir de un individuo pasado como parametro, permite calcular la adaptacion de dicho individuo
# From a given individual as a parameter, it allows to calculate the adaptation of that individual.

def evalKnapsack(individual):

    value = 0.0
    weight = 0.0
    
    # Producto vectorial de un individuo (boolean) por los datos (float) 
    # Multiplica cada bit del individuo por el valor correspondiente en el vector de datos y finalmente hace la suma de todos

    # Vector product of an individual (boolean) by the data (float) 
    # Multiplies each bit of the individual by the corresponding value in the data vector and finally does the sum of all the bits.

    value = np.dot(individual,dm.__values__)
    weight = np.dot(individual,dm.__weights__) # Mismo cáculo para el vector de pesos

#    print("value: ", value)
#    print("weight: ", weight)

    # Se penaliza en caso de que el peso de la mochila exceda el maximo
    # Penalty in case the weight of the backpack exceeds the maximum.
    diff = dm.__knapsackMax__ - weight
    if(diff < 0):
    	value = value + (diff * 10) # OJO: tened en cuenta que diff es negativo, por lo que en realidad está RESTANDO

    return (value,) 
    #OJO: La respuesta tiene que ser una tupla, aunque solo consideremos un valor
    #NOTE: The answer has to be a tuple, even if we only consider one value.

#%% Se comprueba la asignacion de fitness:
# Esta parte solo se incluye como comprobacion de la función evalKnapsack
# No es necesario incluirlo en la evaluacion

# The fitness allocation is checked in this function:
# This part is only included as a check of the evalKnapsack function.
# It is not necessary to include it in the evaluation.

def prueba():

    #Herramienta para guardar la configuracion de la poblacion
    #Tool to save population settings
    toolbox = base.Toolbox()

    evol_simple.ConfiguracionSolucion.configuraPoblacion(toolbox)

    # Se instancia un individuo (aleatorio)
    # One individual (random) is instantiated
    ind = toolbox.individual()
    
    '''
    Se aconseja al alumno probar con varios individuos en diferentes condiciones de optimalidad para comprobar si la función está bien definida en todo el 
    espacio de búsqueda.    
    '''
    '''The student is advised to test with several individuals under different optimality conditions to check if the function is well defined over the whole search space.'''

    # Se imprime el individuo ANTES de evaluar
    # Individual is printed BEFORE evaluating
    print ("\nIndividuo ANTES de evaluar")
    print (ind)
    print (ind.fitness.valid) # False

    ind.fitness.values = evalKnapsack(ind)

    # Se imprime el individuo DESPUES de evaluar
    # Individual is printed AFTER assessing
    print ("\nIndividuo TRAS evaluar")
    print (ind)
    print (ind.fitness.valid) # True
    print (ind.fitness)

if __name__ == "__main__":
    prueba()
