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
#Protected Division (avoids division by 0)
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

#%% Definición de la posible configuración del árbol que representará una solución
# Definition of the possible configuration of the tree that will represent a solution
def configuraIndividuo():

    ''' Para trabajar con arboles de expresiones, primero se deben definir los posibles componentes que puede incluir cada arbol'''
    ''' In order to work with expression trees, we must first define the possible components that each tree can include'''

    #Se crea un conjunto de primitivas
    #A set of primitives is created
    pset = gp.PrimitiveSet("MAIN", 1) #Se inicializa con la raiz
    #It is initialised with the root
    
    #Se añaden las posibles operaciones que se pueden emplear para construirlo
    #The possible operations that can be used to construct it are added.
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protectedDiv, 2) #Está definida arriba
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    ''' Se añade un valor constante (aleatorio) a incluir en el arbol: permite incluir en las funciones otros operandos. 
    Por ejemplo: para elevar o multiplicar o dividir las variables por diferentes numeros'''
    
    ''' A constant (random) value to include in the tree is added: it allows to include in the functions other operands. 
    For example: to exponentiate or multiply or divide the variables by different numbers.'''
    pset.addEphemeralConstant('rand101', lambda: random.randint(-1,1))

    ''' Se añade un argumento para la función a evaluar (en nuestro problema solo hay una: la 'x' de la función). 
    Es decir, dada una x, se pide calcular la y correspondiente.
    Si la función necesitara de más parametros de entrada, se añaden aquí'''
    
    ''' An argument is added for the function to be evaluated (in our problem there is only one: the 'x' of the function). 
    That is, given an x, you are asked to calculate the corresponding y.
    If the function needs more input parameters, they are added here'''
    pset.renameArguments(ARG0='x')

    return pset

#%% Definición del objetivo
# Definition of the objective
def configuraPoblacion(toolbox):

    ''' Se configura el fitness que se va a emplear en los individuos
	 En este caso se configura para:
	 1.buscar un único objetivo: es una tupla de solo un numero
	 2.minimizar ese objetivo (se multiplica por un negativo)
     Lo que queremos es minimizar el error de la funcion'''
    ''' The fitness to be used for the individuals is configured.
	 In this case it is configured to:
	 1.search for a single target: it is a tuple of only one number.
	 2.minimise that target (it is multiplied by a negative).
     What we want is to minimise the error of the function'''
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

    ''' Se configura el individuo para que utilice la descripción anterior de fitness dentro de los individuos '''
    ''' The individual is configured to use the above description of fitness within individuals '''
    creator.create("Individual",  gp.PrimitiveTree, fitness=creator.FitnessMin)

#%% Definición de los individuos
# Definition of individuals

    pset = configuraIndividuo()

    # Se define cada gen del genotipo como una expresión
    # La incialización se hará de forma Intermedia (ver teoría) con una altura de entre 1 y 2
    
    # Each gene of the genotype is defined as an expression.
    # Initialisation will be done in an Intermediate form (see theory) with a height of between 1 and 2
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    # En lugar de atributos numéricos, el genotipo contendrá árboles de expresiones
    # Instead of numeric attributes, the genotype shall contain expression trees.
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # Para poder evaluar el resultado de los los arboles, esta funcion permite leerlos y convertirlos en expresiones aritmeticas en python
    # In order to evaluate the result of the trees, this function allows to read them and convert them into arithmetic expressions in python.
    toolbox.register("compile", gp.compile, pset=pset)

    return pset

''' Se comprueba que los individuos están correctamente definidos. 
No es necesario incluirlo en el experimento final'''

''' Check that the individuals are correctly defined. 
It is not necessary to include it in the final experiment'''

#%% Se comprueba el resultado de generar un individuo
def pruebaIndividuo():
    
    pset = configuraIndividuo()
    # Realiza una incialización completa con profundida entre 1 y 3
    # Performs a full initialisation with depth between 1 and 3
    expr = gp.genFull(pset, min_=1, max_=3) 
    # Obtiene el arbol correspondiente
    # Extracts the corresponding tree
    tree = gp.PrimitiveTree(expr)
    # Se visualiza como una lista de operaciones
    # Displayed as a list of operations
    print(tree)

#%% Se comprueba el resultado de generar una poblacion completa
def pruebaPoblacion():

    toolbox = base.Toolbox()
    
    configuraPoblacion(toolbox)
    
    # Se inicializa la poblacion. Tendrá un total de 10 individuos.
    pop = toolbox.population(n=10)

    # Se imprime la población: 10 individuos como arboles de expresiones
    for ind in pop:
        print(gp.PrimitiveTree(ind))

if __name__ == "__main__":
    #pruebaIndividuo()
    pruebaPoblacion()