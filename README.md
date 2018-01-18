# Computación Neuronal y Evolutiva

## [Grado en Ingeniería Informática](http://www.ubu.es/grado-en-ingenieria-informatica "Grado en Ingeniería Informática")
## Universidad de Burgos

El repositorio contiene el código pyhton necesario para ejecutar varios problemas simples de computacion evolutiva, empleando la librería [DEAP](https://github.com/DEAP/deap "DEAP GitHub").

Todos los ficheros están comentados para ayudar a comprender la solución propuesta.

Cada uno de los ficheros contiene una estructura similar: En primer lugar incluye la función o funciones que se emplean en la solucion. En segundo lugar una fucnión que llama a la primera y muestra su resultado. De esa forma, cada uno puede ser ejecutado de forma individual y comprobar cuál es el resultado que genera. 

A medida que se completa el problema, varios modulos importan el contenido de los modulos anteriores y utilizan las funciones definidas en estos para completar su ejecución. De ahí que se recomiende el analizar el contenido de forma ordenada.

Se incluyen 3 ejemplos diferentes:

1. En el directorio "evol_simple", se puede ver la configuración básica y ejecución por módulos de un programa python que permite resolver el problema de la mochila  
2. En el directorio "experiments", se emplean los módulos programa anterior para generar un conjunto automático de pruebas para comprobar el efecto de la modificación de los parámetros del algoritmo evolutivo sobre las respuestas que se obtienen  
3. En el directorio "genetic_prog", se puede ver la configuración básica y ejecución por módulos de un programa python que permite resolver un problema sencillo de regresión simbólica (calcular una función polinómica dados sus resultados)  

--- 
