## Explicación de la Configuración

El fichero `cartpole_neat.ini` configura cómo NEAT crea, evalúa y evoluciona las redes neuronales. En este ejemplo, cada red recibe las cuatro observaciones de CartPole y produce una salida que el script convierte en una de las dos acciones posibles; puedes ver ese uso en `cartpole_neat.py`.

### `[NEAT]`: población y criterio de parada

- `fitness_criterion = max`: usa la aptitud máxima de la población para evaluar si se alcanzó el objetivo.
- `fitness_threshold = 475`: umbral de aptitud que permite detener la ejecución antes de llegar al límite de generaciones. Es un objetivo alto para CartPole, cuyo episodio puede durar hasta 500 pasos.
- `pop_size = 50`: cantidad de genomas —candidatos de red— por generación.
- `reset_on_extinction = False`: no reinicia automáticamente la población si desaparecen todas las especies.
- `no_fitness_termination = False`: permite que la aptitud alcance el umbral y detenga la evolución.

### `[DefaultGenome]`: estructura y parámetros de las redes

**Tamaño y topología**

- `num_inputs = 4`, `num_outputs = 1`, `num_hidden = 0`: cuatro entradas, una salida y ningún nodo oculto inicial.
- `feed_forward = True`: no se permiten conexiones recurrentes; la red no tiene memoria interna.
- `initial_connection = full`: empieza con conexiones completas entre las entradas y las salidas. Como no hay nodos ocultos, la red inicial es directa.
- `conn_add_prob = 0.5`, `conn_delete_prob = 0.3`: probabilidades de añadir o eliminar conexiones durante las mutaciones.
- `node_add_prob = 0.2`, `node_delete_prob = 0.1`: probabilidades de añadir o eliminar nodos.
- `enabled_default = True`, `enabled_mutate_rate = 0.01`: las conexiones empiezan activas y pueden cambiar de estado mediante mutación.

**Funciones de activación y agregación**

- `activation_default = tanh` y `aggregation_default = sum`: la función de activación predeterminada es tangente hiperbólica y las entradas de cada nodo se suman.
- Las opciones contienen únicamente `tanh` y `sum`, y sus tasas de mutación son `0.0`; por tanto, esos comportamientos no cambian durante la evolución.

**Sesgo, pesos y respuesta de los nodos**

- `bias_*` controla el sesgo: distribución inicial (`init_mean`, `init_stdev`), límites (`min_value`, `max_value`) y cómo puede cambiar (`mutate_power`, `mutate_rate`, `replace_rate`).
- `weight_*` aplica el mismo tipo de controles a los pesos de las conexiones.
- `response_*` configura la respuesta o sensibilidad de los nodos. Aquí empieza en `1.0` y todas sus tasas de mutación son `0.0`, así que permanece fija.

En las tasas de mutación, `mutate_rate` determina con qué frecuencia se modifica un valor y `replace_rate` con qué frecuencia se sustituye por otro. `mutate_power` controla la magnitud de los cambios; los límites evitan que los valores excedan el rango indicado. En esta configuración, pesos y sesgos sí pueden evolucionar, pero la activación, la agregación y la respuesta quedan fijas.

**Distancia genética**

- `compatibility_disjoint_coefficient = 1.0` y `compatibility_weight_coefficient = 0.5`: ponderan diferencias de estructura y de pesos al calcular la distancia entre genomas. Esa distancia ayuda a decidir qué genomas pertenecen a la misma especie.

### `[DefaultSpeciesSet]`: agrupación en especies

- `compatibility_threshold = 3.0`: umbral de distancia genética para agrupar genomas en una especie. Agrupar candidatos similares ayuda a proteger estructuras nuevas mientras compiten con otras.

### `[DefaultStagnation]`: estancamiento de especies

- `species_fitness_func = max`: la aptitud de una especie se representa con la de su mejor miembro.
- `max_stagnation = 15`: una especie que no mejora durante ese número de generaciones puede considerarse estancada.
- `species_elitism = 1`: protege de la eliminación a la especie más destacada.

### `[DefaultReproduction]`: reproducción y supervivencia

- `elitism = 2`: conserva los dos mejores genomas de cada especie sin modificarlos al formar la siguiente generación.
- `survival_threshold = 0.2`: limita al 20 % superior de cada especie el conjunto de candidatos elegibles para reproducirse.

**En conjunto**, es una configuración pequeña, con 50 candidatos por generación y hasta 50 generaciones según el script. Evoluciona principalmente la topología y los pesos y sesgos, buscando alcanzar una aptitud de 475 antes del límite de generaciones.