import math
import operator
import random
import time

import numpy as np
from deap import algorithms, base, creator, gp, tools

import CartPole_env as env

# La raíz del árbol devuelve una acción CartPole válida: 0 o 1.
def score_to_action(score: float) -> int:
    """Convierte una puntuación real en una de las dos acciones de CartPole."""
    return int(score > 0)


def protected_div(left: float, right: float) -> float:
    """División protegida frente a divisiones por cero."""
    try:
        return left / right
    except ZeroDivisionError:
        return 1.0


toolbox = base.Toolbox()
stats = tools.Statistics(key=lambda individual: individual.fitness.values)


def configure_experiment():
    # Nombres propios para poder importar este módulo junto al ejemplo sin tipar.
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))

    if not hasattr(creator, "Individual"):
        creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

    # Cuatro observaciones reales como entradas; la política debe devolver int.
    pset = gp.PrimitiveSetTyped("MAIN", [float, float, float, float], int)
    
    pset.renameArguments(
        ARG0="cart_position",
        ARG1="cart_velocity",
        ARG2="pole_angle",
        ARG3="pole_angular_velocity",
    )

    # Primitivas internas: todas reciben y devuelven valores float.
    pset.addPrimitive(operator.add, [float, float], float)
    pset.addPrimitive(operator.sub, [float, float], float)
    pset.addPrimitive(operator.mul, [float, float], float)
    pset.addPrimitive(protected_div, [float, float], float)
    pset.addPrimitive(operator.neg, [float], float)
    pset.addPrimitive(math.cos, [float], float)
    pset.addPrimitive(math.sin, [float], float)

    # Única primitiva que produce la salida int; garantiza que sea 0 o 1.
    pset.addPrimitive(score_to_action, [float], int)

    # Terminales necesarios para generar o mutar subárboles int.
    # Son exactamente las acciones válidas de CartPole.
    pset.addTerminal(0, int)
    pset.addTerminal(1, int)

    # Constantes reales para que coincidan con los tipos de las primitivas.
    pset.addEphemeralConstant(
        "randFloat",
        lambda: float(random.randint(-1, 1)),
        float,
    )

    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
    toolbox.register("individual",  tools.initIterate, creator.Individual, toolbox.expr)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("compile", gp.compile, pset=pset)
    toolbox.register("evaluate", evaluate_individual)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    toolbox.decorate(
        "mate",
        gp.staticLimit(key=operator.attrgetter("height"), max_value=17),
    )
    toolbox.decorate(
        "mutate",
        gp.staticLimit(key=operator.attrgetter("height"), max_value=17),
    )

    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    return pset

def evaluate_individual(individual):
    func = toolbox.compile(expr=individual)
    return env.evaluate_policy(
        lambda obs: func(*obs),
        n_episodes=5,
        episode_len=500,
    )


def run_experiment():
    configure_experiment()

    population = toolbox.population(n=80)
    crossover_probability = 0.75
    mutation_probability = 0.1
    generations = 50

    print("Start of evolution")
    start = time.time()

    population, logbook = algorithms.eaSimple(
        population,
        toolbox,
        crossover_probability,
        mutation_probability,
        generations,
        stats=stats,
    )

    print("-- End of evolution --")
    print(f"Time taken = {time.time() - start:.4f} seconds")
    best_individual = tools.selBest(population, 1)[0]
    print("Best individual:", best_individual, best_individual.fitness.values)
    best_func = toolbox.compile(expr=best_individual)
    env.run_best_policy(lambda obs: best_func(*obs))
    
if __name__ == "__main__":
    run_experiment()