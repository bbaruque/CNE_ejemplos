# -*- coding: utf-8 -*-
"""
Este módulo permite incorporar medidas estadísticas al proceso evolutivo, que luego se pueden recuperar.
Esto permite estimar si la evolución progresa de forma correcta o no.

This module allows statistical measures to be incorporated into the evolutionary process, which can then be retrieved.
This makes it possible to estimate whether the evolution is progressing correctly or not.


@author: bbaruque
"""

import sys
sys.path.append('.')

import matplotlib.pyplot as plt
import numpy as np 

from deap import base, tools

import CicloEvolutivo

#%%
def configuraEstadisticasEvolucion():

    # Se configura que estadísticas se quieren analizar sobre la evolucion
    # We set up which statistics you want to analyse on the evolution
    stats = tools.Statistics(lambda ind: ind.fitness.values) 
    stats.register("avg", np.mean) 
    stats.register("std", np.std) 
    stats.register("min", np.min) 
    stats.register("max", np.max) 
    
    return stats
    
#%% Visualizamos una estadística para comprobar como fue la evolucion
# We visualise a statistic to check how it evolved.
def visualizaGrafica(log):

    # Se recuperan los datos desde el log
    # Data is retrieved from the log
    gen = log.select("gen")
    avgs = log.select("avg")
    
    # Se establece una figura para dibujar
    # A figure is set to draw
    fig, ax1 = plt.subplots()
    
    # Se representa la media del valor de fitness por cada generación
    # The average fitness value is plotted for each generation.
    line1 = ax1.plot(gen, avgs, "r-", label="Average Fitness")    
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    
    ''' Notad que se deberían representar mas cosas. Por ejemplo el maximo y el minimo de ese fitness se están recogiendo en las estadisticas, aunque en el ejemplo no se representen '''
    ''' Note that additional information should be represented. For example, the maximum and minimum of that fitness are being collected in the statistics, although in the example they are not represented'''

    plt.plot()

#%%
if __name__ == "__main__":
    # Herramienta para guardar la configuracion de la ejecucion
    # Tool to save the execution settings
    toolbox = base.Toolbox()

    # Se configura que estadísticas se quieren analizar sobre la evolucion
    # We set up which statistics we want to analyse on the evolution
    stats = configuraEstadisticasEvolucion()

    # Se ejecuta la evolución y se recupera el log de datos de lo que ha sucedido en la evolucion
    # The evolution is executed and the data log of what has happened in the evolution is retrieved
    log = CicloEvolutivo.realizaEvolucion(toolbox, stats)
    visualizaGrafica(log)
