El siguiente repositorio contiene el código pyhton necesario para ejecutar un algoritmo genético básico que resuelve el clasico [problema de la mochila](https://es.wikipedia.org/wiki/Problema_de_la_mochila "Wikipedia"), empleando la librería [DEAP](https://github.com/DEAP/deap "DEAP GitHub").

Se han separado los ficheros fuente por funcionalidad, para simplificar las explicaciones en cada uno. No es obligatorio seguir exáctamente la misma distribución de funcionalidad.
Para una mejor comprensión de la solución del problema, se sugiere el siguiente orden de lectura:

1. DescripcionProblema.md
2. DatosMochila.py
4. ConfiguracionSolucion.py
5. Evaluacion.py
6. CicloEvolutivo.py
7. EstadisticasEvolucion.py

Cada uno de los ficheros contiene una estructura similar: En primer lugar incluye la función o funciones que se emplean en la solución. En segundo lugar una función que llama a la primera y muestra su resultado. De esa forma, cada uno puede ser ejecutado de forma individual y comprobar cuál es el resultado que genera. 

A medida que se va completando el problema, varios modulos importan el contenido de los modulos anteriores y utilizan las funciones definidas en éstos para completar su propia ejecución. De ahí que se recomiende el analizar el contenido de forma ordenada.
