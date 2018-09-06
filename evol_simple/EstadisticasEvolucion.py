# -*- coding: utf-8 -*-
"""
Este módulo permite incorporar medidas estadísticas al proceso evolutivo, que luego se pueden recuperar.
Esto permite estimar si la evolución progresa de forma correcta o no.

@author: bbaruque
"""

from deap import base, tools
import CicloEvolutivo
import matplotlib.pyplot as plt

def configuraEstadisticasEvolucion():

    import numpy as np 
    
    # Se configura que estadísticas se quieren analizar sobre la evolucion
    stats = tools.Statistics(lambda ind: ind.fitness.values) 
    stats.register("avg", np.mean) 
    stats.register("std", np.std) 
    stats.register("min", np.min) 
    stats.register("max", np.max) 
    
    return stats
    
    #%% Visualizamos una estadística para comprobar como fue la evolucion
def visualizaGrafica(log):
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
    # Herramienta para guardar la configuracion de la ejecucion
    toolbox = base.Toolbox()
    # Se configura que estadísticas se quieren analizar sobre la evolucion
    stats = configuraEstadisticasEvolucion()
    # Se ejecuta la evolución y se recupera el log de datos de lo que ha sucedido en la evolucion
    log = CicloEvolutivo.realizaEvolucion(toolbox, stats)
    visualizaGrafica(log)
