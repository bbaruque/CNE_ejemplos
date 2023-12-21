# -*- coding: utf-8 -*-
"""
@author: bbaruque
"""

import sys
sys.path.append('./evol_simple')
sys.path.append('./experiments')

from deap import base
import evol_simple.CicloEvolutivo
import experiments.LecturaDatos

if __name__ == "__main__":
   
    toolbox = base.Toolbox()
    
    # Se debe permitir cambiar el fichero de entrada de datos facilmente
    experiments.LecturaDatos.carga_datos('./experiments/datos/datos2.csv')    
    evol_simple.CicloEvolutivo.realizaEvolucion(toolbox,[])
    
    # Se deberán incluir los metodos necesarios para almacenar la solución
    # Es importante asegurarse de que el formato es correcto:
    # parte de la nota dependerá de que se pueda leer correctamente al corregir