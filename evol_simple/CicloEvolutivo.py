# -*- coding: utf-8 -*-
"""
Este modulo contiene las funciones necesarias para llamar a las funciones de los modulos anteriores y configurar y lanzar una ejecución de un algoritmo evolutivo que permita alcanzar la solución óptima al problema de la mochila.

This module contains the necessary functions to call the functions of the previous modules and to configure and launch an execution of an evolutionary algorithm to yield the optimal solution to the knapsack problem.

@author: bbaruque
"""

import sys
sys.path.append('.')

from deap import base, tools
from deap import algorithms

import ConfiguracionSolucion
import EvaluacionSolucion

#%% Se Define la configuracion del algoritmo genetico
# Genetic algorithm configuration is defined.
def configuracionAlgoritmo(toolbox):  
    # Se seleccionan procedimiento standard para cruce, mutacion y seleccion
    # Standard procedures for crossover, mutation and selection are selected.
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

	# Se define cómo se evaluará cada individuo
	# En este caso, se hará uso de la función de evaluación que se ha definido en el modulo EvaluacionSolucion.py

    # We define how each individual will be evaluated
	# In this case, we will make use of the evaluation function that has been defined in the module EvaluacionSolucion.py.
    toolbox.register("evaluate", EvaluacionSolucion.evalKnapsack)

#%% Se define como se realiza la Evolución de la busqueda de la solución
# Evolution of the search for a solution is defined as follows
def realizaEvolucion(toolbox, stats):

    # Se configura cómo se define cada individuo. Ver fichero correspondiente.
    # How each individual is defined is configured. See corresponding file.
    ConfiguracionSolucion.configuraPoblacion(toolbox)

    configuracionAlgoritmo(toolbox)

    # Se inicializa la poblacion con 300 individuos
    # The population is initialised with 300 individuals.
    population = toolbox.population(n=300)

    # Se llama al algoritmo que permite la evolucion de las soluciones
    # The algorithm that allows the evolution of the solutions is called
    population, logbook = algorithms.eaSimple(population, toolbox, 
	                               cxpb=0.5, mutpb=0.2, # Probabilidades de cruce y mutacion
	                               ngen=20, verbose=False, stats=stats) # Numero de generaciones a completar y estadisticas a recoger

    # Por cada generación, la estructura de logbook va almacenando un resumen de los avances del algoritmo.
    # For each generation, the logbook structure stores a summary of the algorithm's progress.
    print("El resultado de la evolución es: ")
    print(logbook)

    # Comprobamos cual es la mejor solucion encontrada por evolucion
    # We check which is the best solution found by evolution
    print("La mejor solucion encontrada es: ")
    print(tools.selBest(population,1)[0])
    
    return logbook

#%%
if __name__ == "__main__":
    
    # Herramienta para guardar la configuracion de la ejecucion
    # Tool to save the execution settings
    toolbox = base.Toolbox()
    realizaEvolucion(toolbox,[])