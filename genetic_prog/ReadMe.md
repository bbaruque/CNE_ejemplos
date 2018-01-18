El siguiente repositorio contiene el código pyhton necesario para ejecutar un algoritmo de programación genética que resuelve un problema simple de regresión simbólica (aproximación a una función), empleando la librería [DEAP] (https://github.com/DEAP/deap "DEAP GitHub").

Se han separado los ficheros fuente por funcionalidad, para simplificar las explicaciones en cada uno. Para una mejor comprensión de la solución del problema, se sugiere el siguiente orden de lectura:

1. DescripcionProblema.md
2. DatosMochila.py
4. ConfiguracionProblema.py
5. Evaluacion.py
6. CicloEvolutivo.py
7. EstadisticasEvolucion.py

Cada uno de los ficheros contiene una estructura similar: En primer lugar incluye la función o funciones que se emplean en la solucion. En segundo lugar una fucnión que llama a la primera y muestra su resultado. De esa forma, cada uno puede ser ejecutado de forma individual y comprobar cuál es el resultado que genera. 

A medida que se completa el problema, varios modulos importan el contenido de los modulos anteriores y utilizan las funciones definidas en éstos para completar su ejecución. De ahí que se recomiende el analizar el contenido de forma ordenada.
