import random
import math
import operator
import numpy as np
import time

from deap import base, creator, algorithms, gp
from deap import tools

import CartPole_env as env

toolbox = base.Toolbox()
# Creation of the Statistics object to calculate stats for each generation
stats = tools.Statistics(key=lambda ind: ind.fitness.values)


def protectedDiv(left, right):
    """Protected division (avoids division by zero)."""
    try:
        return left / right
    except ZeroDivisionError:
        return 1.0


def configuraIndividuo():
    """Define the primitive set for CartPole expression trees (4 observation inputs)."""
    pset = gp.PrimitiveSet("MAIN", 4)
    pset.renameArguments(
        ARG0="cart_position",
        ARG1="cart_velocity",
        ARG2="pole_angle",
        ARG3="pole_angular_velocity",
    )

    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protectedDiv, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))

    return pset


def evaluate_individual(individual):
    func = toolbox.compile(expr=individual)
    return env.evaluate_policy(
        lambda obs: int(func(*obs) > 0),
        n_episodes=5,
        episode_len=500,
    )


def configure_experiment():
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

    pset = configuraIndividuo()

    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)

    toolbox.register("evaluate", evaluate_individual)

    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)


def run_experiment():
    configure_experiment()

    pop = toolbox.population(n=80)
    CXPB, MUTPB, NGEN = 0.75, 0.1, 50

    print("Start of evolution")
    start = time.time()
    pop, logbook = algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, NGEN, stats=stats)
    end = time.time()

    print("-- End of (successful) evolution --")
    print("Time taken = %4.4f seconds" % (end - start))

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

    best_func = toolbox.compile(expr=best_ind)
    env.run_best_policy(lambda obs: int(best_func(*obs) > 0))


if __name__ == "__main__":
    run_experiment()