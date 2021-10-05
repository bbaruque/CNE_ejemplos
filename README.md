# Computación Neuronal y Evolutiva

## [Grado en Ingeniería Informática](http://www.ubu.es/grado-en-ingenieria-informatica "Grado en Ingeniería Informática")
![Universidad de Burgos](https://www.ubu.es/sites/all/themes/ubu_theme/images/UBUEscudo-1910.png)  
## [Universidad de Burgos](http://www.ubu.es) 

El repositorio contiene el código pyhton necesario para ejecutar varios problemas simples de computacion evolutiva, empleando la librería [DEAP](https://github.com/DEAP/deap "DEAP GitHub").

Todos los ficheros están comentados para ayudar a comprender la solución propuesta.

Cada uno de los ficheros contiene una estructura similar: En primer lugar incluye la función o funciones que se emplean en la solución. En segundo lugar una función que llama a la primera y muestra su resultado. De esa forma, cada fichero puede ser ejecutado de forma individual y comprobar cuál es el resultado que genera. 

A medida que se completa el problema, varios modulos importan el contenido de los modulos anteriores y utilizan las funciones definidas en estos para completar su ejecución. De ahí que se recomiende el analizar el contenido de forma ordenada.

Se incluyen 3 ejemplos diferentes:

1. En el directorio "evol_simple", se puede ver la configuración básica y ejecución por módulos de un programa python que permite resolver el problema de la mochila  
2. En el directorio "experiments", se emplean los módulos programa anterior para generar un conjunto automático de pruebas para comprobar el efecto de la modificación de los parámetros del algoritmo evolutivo sobre las respuestas que se obtienen  
3. En el directorio "genetic_prog", se puede ver la configuración básica y ejecución por módulos de un programa python que permite resolver un problema sencillo de regresión simbólica (calcular una función polinómica dados sus resultados)  

--- 

# Neural and Evolutionary Computation

## [Degree in Computer Science](http://www.ubu.es/grado-en-ingenieria-informatica "Grado en Ingeniería Informática")
![Universidad de Burgos](https://www.ubu.es/sites/all/themes/ubu_theme/images/UBUEscudo-1910.png)
## [University of Burgos](http://www.ubu.es)

The repository contains the pyhton code needed to run several simple evolutionary computation problems, using the [DEAP](https://github.com/DEAP/deap "DEAP GitHub") library.

All files are commented to help understand the proposed solution.

Each of the files contains a similar structure: Firstly it includes the function or functions that are used in the solution. Secondly, a function that calls the first one and displays its result. In this way, each file can be executed individually and the result generated can be checked. 

As the problem is completed, several modules import the content of the previous modules and use the functions defined in them to complete their execution. Hence, it is recommended to analyse the content in an orderly fashion.

Three different examples are included:

1. In the "evol_simple" directory, you can see the basic configuration and execution by modules of a python program that allows to solve the knapsack problem.  
2. In the "experiments" directory, the previous program modules are used to generate an automatic set of tests to check the effect of the modification of the parameters of the evolutionary algorithm on the answers obtained.  
3. In the "genetic_prog" directory, you can see the basic configuration and execution by modules of a Python program that allows you to solve a simple symbolic regression problem (calculating a polynomial function given its results).  

