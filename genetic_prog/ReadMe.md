El siguiente repositorio contiene el código pyhton necesario para ejecutar un algoritmo de programación genética que resuelve un problema simple de regresión simbólica (aproximación a una función), empleando la librería [DEAP] (https://github.com/DEAP/deap "DEAP GitHub").

Se han separado los ficheros fuente por funcionalidad, para simplificar las explicaciones en cada uno. Para una mejor comprensión de la solución del problema, se sugiere el siguiente orden de lectura:

1. DescripcionProblema.md
2. DatosFuncion.py
4. ConfiguracionProblema.py
5. Evaluacion.py
6. CicloEvolutivo.py
7. EstadisticasEvolucion.py

Cada uno de los ficheros contiene una estructura similar: En primer lugar incluye la función o funciones que se emplean en la solucion. En segundo lugar una fucnión que llama a la primera y muestra su resultado. De esa forma, cada uno puede ser ejecutado de forma individual y comprobar cuál es el resultado que genera. 

A medida que se completa el problema, varios modulos importan el contenido de los modulos anteriores y utilizan las funciones definidas en éstos para completar su ejecución. De ahí que se recomiende el analizar el contenido de forma ordenada.

-----

The following repository contains the Pyhton code needed to run a genetic programming algorithm that solves a simple symbolic regression problem (approximation to a function), using the [DEAP library](https://github.com/DEAP/deap "DEAP GitHub").

The source files have been separated by functionality, in order to simplify the explanations in each one. For a better understanding of the solution of the problem, the following reading order is suggested:

1. DescripcionProblema.md
2. DatosFuncion.py
4. ConfiguracionProblema.py
5. Evaluacion.py
6. CicloEvolutivo.py
7. EstadisticasEvolucion.py

Each of the files contains a similar structure: Firstly it includes the function or functions that are used in the solution. Secondly, a function that calls the first one and displays its result. In that way, each one can be executed individually and the result generated can be checked. 

As the problem is completed, several modules import the content of the previous modules and use the functions defined in them to complete their execution. Hence, it is recommended to analyse the content in an orderly fashion.
