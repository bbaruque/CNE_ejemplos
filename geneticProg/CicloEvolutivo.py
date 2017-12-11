# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:20:04 2017

@author: bbaruque
"""

from deap import base, tools
from deap import gp
from deap import algorithms

import operator

import ConfiguracionProblema
import Evaluacion

#%% Se Define la configuracion del algoritmo genetico
def configuracionAlgoritmo(toolbox, pset):  
    
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    
	# Se define cómo se evaluará cada individuo
	# En este caso, se hará uso de la función de evaluación que se ha definido en el modulo contiguo
    toolbox.register("evaluate", Evaluacion.evalEcuacion, toolbox)
    
#%% Se define como se realiza la Evolución de la Solución
def realizaEvolucion(stats):

    '''Herramienta para guardar la configuracion de la poblacion'''
    toolbox = base.Toolbox()

    pset = ConfiguracionProblema.configuraPoblacion(toolbox)

    configuracionAlgoritmo(toolbox, pset)

    # Se inicializa la poblacion
    population = toolbox.population(n=50)

    # Se llama al algoritmo que permite la evolucion de las soluciones
    population, logbook = algorithms.eaSimple(population, toolbox, 
	                               cxpb=0.5, mutpb=0.2, # Probabilidades de cruce y mutacion
	                               ngen=30, verbose=False, stats=stats) # Numero de generaciones a completar

    print(logbook)
    best = tools.selBest(population,1)[0]
    
    print("La mejor solucion encontrada es: ")
    print(best)
	
	# TODO Sería interesante poder mostrar el resultado final como un árbol
    Evaluacion.plotExpressionTree(toolbox, best)


    return logbook

if __name__ == "__main__":
    realizaEvolucion([])