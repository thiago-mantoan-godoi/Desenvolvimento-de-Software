import random
import numpy as np
from deap import base, creator, tools, algorithms
from fitness import fitness_function

def configure_ga():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, 0, 100)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", fitness_function)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutPolynomialBounded, low=0.0, up=100.0, eta=20.0, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    
    return toolbox

def run_ga(toolbox, n_gen=100, n_pop=50):
    random.seed(42)
    pop = toolbox.population(n=n_pop)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=n_gen, stats=stats, halloffame=hof, verbose=True)
    
    return pop, stats, hof
