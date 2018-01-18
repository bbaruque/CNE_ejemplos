# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:56:47 2017

@author: bbaruque
"""

import random

from deap import base, creator
from deap import tools

def configuraPoblacion(toolbox):

	''' Se configura el fitness que se va a emplear en los individuos
	 En este caso se configura para:
	 1.buscar un único objetivo: es una tupla de solo un numero
	 2.maximizar ese objetivo (se multiplica por un positivo)'''
	creator.create("FitnessMax", base.Fitness, weights=(1.0,))

	''' Se configura el individuo para que utilice la descripción anterior
	de fitness dentro de los individuos '''
	creator.create("Individual", list, fitness=creator.FitnessMax)

	''' Ejemplo de genotipo cuyos genes son de tipo float '''
	#toolbox.register("attribute", random.random)
	''' Ejemplo de Genotipo cuyos genes son de tipo booleano '''
	toolbox.register("attribute", random.randint, 0, 1)
	''' El individuo se crea como una lista (o repeticion) de "attribute", definido justo antes
	Tendrá una longitud de 5 atributos '''
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=5)
	''' La población se crea como una lista de "individual", definido justo antes'''
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)


''' Se comprueba que está correctamente definido. 
No es necesario incluirlo en el experimento final'''

def prueba():

    toolbox = base.Toolbox()
    
    configuraPoblacion(toolbox)
    
    ''' Se genera un único individuo '''
    ind = toolbox.individual()
    print(ind)
    
    ''' Se inicializa la poblacion. Tendrá un total de 10 individuos. 
        Se genera como una lista de individuos '''
    pop = toolbox.population(n=10)
    
    ''' Se imprime la población: 10 individuos de 5 genes cada uno'''
    print(pop)
    
    ''' En este ejemplo, todavía no se incluye la adaptación de cada individuo'''

if __name__ == "__main__":
    prueba()
