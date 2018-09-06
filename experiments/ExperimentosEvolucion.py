# -*- coding: utf-8 -*-
"""
Created on Sun 16/12/2017

@author: bbaruque
"""
from deap import base, algorithms, tools

import sys
sys.path.append('..')
sys.path.append('../evol_simple')

import evol_simple.ConfiguracionSolucion as cp
import evol_simple.CicloEvolutivo as ce
import evol_simple.EstadisticasEvolucion as ee

import LecturaDatos as ld

def configura_experimentos():

    # Herramienta para guardar la configuracion de la ejecucion
    toolbox = base.Toolbox()

    # Se configura cómo se define cada individuo. Ver fichero correspondiente
    cp.configuraPoblacion(toolbox)

    # Se configura los diferentes esquemas del ciclo evolutivo (tipo de selección, cruce,...)
    # Por simplificar se emplea la configuración de otros ejemplos, pero se 
    # puede variar a la hora de configurar los experimentos (y comparar 2 tipos de cruce, p.ej.)
    ce.configuracionAlgoritmo(toolbox)

    experimentos = []

    # Se va a comprobar el efecto de aumentar el nº de generaciones del algoritmo
    ngen = [20, 30, 40, 50]

    # Los experimentos se van a realizar sobre distintas configuraciones del problema
    data_input = ['.\datos1.csv','.\datos2.csv','.\datos3.csv']

    for di in data_input:
        
        for n in ngen:
            
            exp = {}
    
            exp['data_input'] = di
            
            exp['toolbox'] = toolbox
    
            alg_param = {}
            alg_param['cxpb'] = 0.75
            alg_param['mutpb'] = 0.2
            alg_param['pop_size'] = 25
            alg_param['ngen'] = n
    
            exp['alg_param'] = alg_param
    
            experimentos.append(exp)

    '''Consiste en una lista de diccionarios.
    Cada uno de ellos contiene los parámetros de un experimento diferente.
    Idealmente, cada experimento solo varía en un parámetro.'''
    return experimentos

# Recibe una lista de diccionarios, cada uno para un experimento
# Va ejecutando uno por uno, almacenando la población final obtenida y sus estadísticas
def ejecuta_experimentos(experimentos, stats):

    populations = []
    logbooks = []

    for exp in experimentos:

        ld.carga_datos(exp['data_input'])
        toolbox = exp['toolbox']
        alg_param = exp['alg_param']

        init_pop = toolbox.population(n=alg_param['pop_size'])

        population, logbook = algorithms.eaSimple(
            init_pop, toolbox, 
            cxpb=alg_param['cxpb'], 
            mutpb=alg_param['mutpb'], 
            ngen=alg_param['ngen'], 
            verbose=True, stats=stats)

        populations.append(population)
        logbooks.append(logbook)
    
    return populations, logbooks

def visualiza_experimentos(experimentos, populations, logbooks):

    for exp, pop, log in zip(experimentos, populations, logbooks):

        print("Parametros del experimento: ")
        print(exp)
        
        print("La mejor solucion encontrada es: ")
        print(tools.selBest(pop,1)[0])

        ee.visualizaGrafica(log)

if __name__ == "__main__":
    experimentos = configura_experimentos()
    stats = ee.configuraEstadisticasEvolucion()
    pops,logs = ejecuta_experimentos(experimentos,stats)
    visualiza_experimentos(experimentos, pops,logs)