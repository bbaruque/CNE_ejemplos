# Neuroevolución con CartPole

En esta carpeta se reúnen ejemplos para controlar el entorno **CartPole-v1** de Gymnasium. El objetivo es mantener un palo vertical empujando un carro a izquierda o derecha.

En cada paso, el entorno proporciona cuatro valores (posición y velocidad del carro, ángulo y velocidad angular del palo). La política elige una de dos acciones: `0` (empujar a la izquierda) o `1` (empujar a la derecha). Se obtiene recompensa mientras el palo sigue en equilibrio; por eso, una recompensa mayor indica que la política ha mantenido el sistema estable durante más tiempo.

## Preparación

Desde la carpeta raíz del repositorio, crea y activa un entorno virtual e instala las dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install "gymnasium[classic-control]" neat-python stable-baselines3
```

La primera instalación incluye DEAP y NumPy, utilizados por los ejemplos evolutivos. Los paquetes adicionales proporcionan el entorno CartPole con visualización, NEAT y PPO, respectivamente.

Para ejecutar un ejemplo, entra en esta carpeta y lanza el script con Python:

```powershell
cd neuro_evol
python cartpole_testRandom.py
```

Los ejemplos que muestran el entorno abren una ventana gráfica; ejecútalos en un ordenador con escritorio.

## Archivos y recorrido recomendado

1. **`gymnasium_env.py`** — reúne funciones comunes para ejecutar episodios, evaluar una política en varios episodios y mostrar su resultado. Los ejemplos de aprendizaje reutilizan estas funciones.
2. **`cartpole_testRandom.py`** — punto de partida. Escoge acciones al azar e imprime las observaciones y recompensas. Avanza paso a paso al pulsar Enter.
3. **`cartpole_testInteractive.py`** — permite probar el control manual: introduce `6` para empujar a la izquierda o `4` para empujar a la derecha.
4. **`cartpole_evolutionary.py`** — aplica programación genética con DEAP. Evoluciona expresiones matemáticas que transforman las cuatro observaciones en una acción.
5. **`cartpole_evolutionary_typed.py`** — variante de programación genética con tipos explícitos: las operaciones internas producen números reales y la salida se convierte en una acción válida.
6. **`cartpole_reinforced.py`** — entrena una red neuronal mediante PPO, un método de aprendizaje por refuerzo, y después muestra un episodio con la política entrenada.
7. **`cartpole_neat.py`** y **`cartpole_neat.ini`** — evolucionan redes neuronales con NEAT. El fichero `.ini` define la población, la estructura de las redes y los parámetros de evolución; el programa lo carga automáticamente.

En los ejemplos evolutivos y en PPO el programa entrena primero y muestra al final el resultado aprendido. El entrenamiento puede tardar; no es necesario pulsar teclas mientras se está ejecutando.

## Ejecutar otros ejemplos

Desde `neuro_evol`, ejecuta el script que quieras probar:

```powershell
python cartpole_testInteractive.py
python cartpole_evolutionary.py
python cartpole_evolutionary_typed.py
python cartpole_neat.py
python cartpole_reinforced.py
```

Los métodos evolutivos y PPO pueden producir resultados distintos entre ejecuciones. Para comparar algoritmos, observa la recompensa obtenida y recuerda que cada evaluación promedia varios episodios para reducir el efecto del azar.

## Ideas para trabajar en clase

- Compara cuánto dura CartPole con acciones aleatorias, con control manual y con una política entrenada.
- En los programas evolutivos, observa cómo la selección, el cruce y la mutación modifican las políticas.
- Compara la representación de una política mediante una expresión (programación genética) y mediante una red neuronal (NEAT o PPO).
- Cambia los parámetros del algoritmo y analiza su efecto en el tiempo de ejecución y la recompensa.
