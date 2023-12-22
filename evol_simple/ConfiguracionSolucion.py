# -*- coding: utf-8 -*-
"""
Fichero que incluye un ejemplo de las operaciones neesarias para configurar la codificación de las posibles soluciones con las que trabajará el algoritmo evolutivo para resolver el problema.

Se necesita indicar cómo se definen los individuos, el fitness y la población de soluciones y registrar todas estas opciones en las estructuras que proporciona la librería DEAP.

---

File that includes an example of the necessary operations to configure the encoding of the possible solutions that the evolutionary algorithm will work with to solve the problem

It is necessary to indicate how the individuals, the fitness and the population of solutions are defined and to register all these options in the structures provided by the DEAP library.

@author: bbaruque
"""

import sys
sys.path.append('.')

import random

from deap import base, creator
from deap import tools

import evol_simple.DatosMochila as dm

#%%
def configuraPoblacion(toolbox):

	''' Se configura el fitness que se va a emplear en los individuos
	 En este caso se configura para:
	 1.buscar un único objetivo: es una tupla de solo un numero
	 2.maximizar ese objetivo (se multiplica por un num. positivo)'''

	''' The fitness to be used for the individuals is configured.
	 In this case it is configured to:
	 1.search for a single target: it is a tuple of only one number.
	 2.maximise that objective (it is multiplied by a positive number)'''
	creator.create("FitnessMax", base.Fitness, weights=(1.0,))

	''' Se configura el individuo para que utilice la descripción anterior de fitness dentro de los individuos '''
	''' The individual is configured to use the above description of fitness within individuals '''
	creator.create("Individual", list, fitness=creator.FitnessMax)

	''' Ejemplo de genotipo cuyos genes son de tipo float '''
	''' Example of a genotype whose genes are of type float '''
	#toolbox.register("attribute", random.random)
	''' Ejemplo de Genotipo cuyos genes son de tipo booleano '''
	''' Example of a genotype whose genes are of Boolean type '''
	toolbox.register("attribute", random.randint, 0, 1) #En realidad, se indica que serán entereos entre 0 y 1

	''' El individuo se crea como una lista (o repeticion) de "attribute", definido justo antes. Tendrá una longitud de tantos atributos como longitud tenga el vector de pesos definido en el problema'''
	''' The individual is created as a list (or repetition) of "attribute", defined just before. It will have a length of as many attributes as the length of the vector of weights defined in the problem.'''
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=len(dm.__weights__))

	''' La población se crea como una lista de "individual", definido justo antes'''
	''' The population is created as an "individual" list, defined just before '''
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)


#%%%%%%%%%%%%
''' Se comprueba que está correctamente definido. No es necesario incluirlo en el experimento final'''
''' Check that it is correctly defined. It does not need to be included in the final experiment'''

def prueba():

    toolbox = base.Toolbox()
    
    configuraPoblacion(toolbox)
    
    '''Se genera un único individuo '''
    '''A single individual is generated '''
    ind = toolbox.individual()
    print("Individuo: ",ind)
    
    '''Se inicializa la poblacion. Tendrá un total de 10 individuos. Se genera como una lista de individuos. '''
    '''The population is initialised. It will have a total of 10 individuals. It is generated as a list of individuals. '''
    pop = toolbox.population(n=10)
	
    '''Se imprime la población: 10 individuos de 5 genes cada uno'''
    '''The population is printed: 10 individuals of 5 genes each'''
    print("Poblacion: ",pop)
    
    '''En este ejemplo, todavía no se calcula la adaptación de cada individuo'''
    '''In this example, the adaptation of each individual is not yet calculated'''

if __name__ == "__main__":
    prueba()
