# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:25:46 2017

@author: bbaruque
"""
"""
Más información de las funciones en:
    
    https://docs.python.org/3/library/csv.html
    http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    
"""

import csv
import evol_simple.DatosMochila as dm

def carga_datos(ruta_fichero):
    # Se crea un objeto que abre el fichero y representa su contenido
    csvfile = open(ruta_fichero, 'r')
    # Se crea un objeto que formatea el contenido como CSV
    # Se considera el simboo de # como comentario y no se leerá
    #reader = csv.reader(csvfile, delimiter=',')
    reader = csv.reader(filter(lambda row: row[0]!='#', csvfile))

    # Se accede a cada registro del fichero
    for i, row in enumerate(reader):
        if (i==0):
            dm.values = list(map(int, row))
        if (i==1):
            dm.weights = list(map(int, row))
        if (i==2):
            dm.knapsackMax = list(map(int, row))

    # Se cierra el fichero    
    csvfile.close()

def prueba():
    carga_datos('.\datos1.csv')
    print(dm.values)
    print(dm.weights)
    print(dm.knapsackMax)

if __name__ == "__main__":
    prueba()