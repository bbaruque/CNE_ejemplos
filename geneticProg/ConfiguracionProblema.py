# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:56:47 2017

@author: bbaruque
"""

import random
import math
import operator

from deap import base, creator, gp
from deap import tools

#Division protegida (evita la division por 0)
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

#%% Definición de la posible configuración del árbol que representará una solución
def configuraIndividuo():

    ''' Para trabajar con arboles de expresiones, primero se deben definir los
    posibles componentes que puede incluir cada arbol'''

    #Se crea un conjunto de primitivas
    pset = gp.PrimitiveSet("MAIN", 1) #Se inicializa con la raiz
    
    #Se añaden las posibles operaciones que se pueden emplear para construirlo
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protectedDiv, 2) #Está definida arriba
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    ''' Se añade un valor constante (aleatorio) a incluir en el arbol: 
        permite incluir en las funciones otros operandos. Por ejemplo
        para elevar o multiplicar o dividir las variables por diferentes numeros'''
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))

    ''' Se añade un argumento para la función a evlauar (en nuestro problema
    solo hay una: la 'x' de la función). Es decir, dada una x, se pide calcular una y.
    Si la función necesitara de más parametros de entrada, se añaden aquí'''
    pset.renameArguments(ARG0='x')

    return pset

def configuraPoblacion(toolbox):
#%% Definición del objetivo

    ''' Se configura el fitness que se va a emplear en los individuos
	 En este caso se configura para:
	 1.buscar un único objetivo: es una tupla de solo un numero
	 2.minimizar ese objetivo (se multiplica por un negativo)
     Lo que queremos es minimizar el error de la funcion'''
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

    ''' Se configura el individuo para que utilice la descripción anterior
    de fitness dentro de los individuos '''
    creator.create("Individual",  gp.PrimitiveTree, fitness=creator.FitnessMin)

#%% Definición de los individuos

    pset = configuraIndividuo()

    # Se define cada gen del genotipo como una expresión
    # La incialización se hará de forma Intermedia (ver teoría) con una altura de entre 1 y 2
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    # En lugar de atributos numéricos, el genotipo contendrá árboles de expresiones
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # Para poder evaluar el resultado de los los arboles, esta funcion permite 
    # leerlos y convertirlos en expresiones aritmeticas en python
    toolbox.register("compile", gp.compile, pset=pset)

    return pset

''' Se comprueba que los individuos están correctamente definidos. 
No es necesario incluirlo en el experimento final'''
#%% Se comprueba el resultado de generar un individuo
def pruebaIndividuo():
    
    pset = configuraIndividuo()
    # Realiza una incialización completa con profundida entre 1 y 3
    expr = gp.genFull(pset, min_=1, max_=3) 
    # Obtiene el arbol correspondiente
    tree = gp.PrimitiveTree(expr)
    # Se visualiza como una lista de operaciones
    print(tree)

#%% Se comprueba el resultado de generar una poblacion completa
def pruebaPoblacion():

    toolbox = base.Toolbox()
    
    configuraPoblacion(toolbox)
    
    # Se inicializa la poblacion. Tendrá un total de 10 individuos.
    pop = toolbox.population(n=10)

    # Se imprime la población: 10 individuos como arboles de expresiones
    print(pop)

if __name__ == "__main__":
    pruebaPoblacion()