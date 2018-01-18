# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:20:04 2017

@author: bbaruque
"""

from deap import tools
import CicloEvolutivo
import matplotlib.pyplot as plt

def visualizaEstadisticasEvolucion():

    import numpy as np 
    
    # Se configura que estadísticas se quieren analizar 
    stats = tools.Statistics(lambda ind: ind.fitness.values) 
    stats.register("avg", np.mean) 
    stats.register("std", np.std) 
    stats.register("min", np.min) 
    stats.register("max", np.max) 
    
    log = CicloEvolutivo.realizaEvolucion(stats)
    
    #%% Visualizamos una estadística para comprobar como fue la evolucion
    
    # Se recuperan los datos desde el log
    gen = log.select("gen")
    avgs = log.select("avg")
    
    # Se establece una figura para dibujar
    fig, ax1 = plt.subplots()
    
    # Se representa la media del valor de fitness por cada generación
    line1 = ax1.plot(gen, avgs, "r-", label="Average Fitness")    
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    
    ''' Notad que se pueden representar mas cosas. Por ejemplo el maximo y el minimo de
    ese fitness se están recogiendo en las estadisticas, aunque en el ejemplo no se
    representen '''
    
    plt.plot()

if __name__ == "__main__":
    visualizaEstadisticasEvolucion()