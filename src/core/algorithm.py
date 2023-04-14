import time

from core.population import Population
from common.config import *
import matplotlib.pyplot as plt
import numpy as np

class EvolutionaryAlgorithm:
    """
    Represents an evolutionary algorithm for solving the problem of determining the optimal number of telecommunication
    towers, their location coordinates, and the bandwidth required for each tower, while considering the initial
    construction cost and maintenance cost based on the bandwidth.
    """

    def __init__(self):
        """
        Initializes the algorithm with input data from files.

        Args:
            blocks_population_file (str): File containing the blocks population data.
            problem_config_file (str): File containing the problem configuration data.
        """
        pass

    def evolve(self, generation_count: int):
        """
        Evolves the population for a certain number of generations or until a stopping criterion is met.

        Args:
            generation_count (int): Number of generations to evolve.
            stopping_criterion (float): Stopping criterion for terminating the evolution process.

        Returns:
            None
        """
        generations = np.arange(generation_count)
        generations_max_fitness = np.arange(generation_count)
        generations_max_fitness = generations_max_fitness.astype(np.float64)

        population = Population.initialize()
        population.evaluate_fitness()

        for generation in range(generation_count):
            # print("selected_chromosomes")
            selected_chromosomes = population.select_chromosomes()
            # print([len(set(ch.genes)) for ch in selected_chromosomes])
            # print()
            new_generation = Population(selected_chromosomes)

            print("crossover")
            new_generation = new_generation.crossover(CROSSOVER_RATE)
            print([len(set(ch.genes)) for ch in new_generation.chromosomes])
            print()

            new_generation.mutate(MUTATION_RATE)

            new_generation.evaluate_fitness()

            print("replace")
            population.replace(new_generation)  # this changes the allocations
            print([len(set(ch.genes)) for ch in population.chromosomes])
            print()
            max_fitness = max(population.chromosomes, key=lambda x: x.fitness).fitness
            print(max_fitness)
            generations_max_fitness[generation] = max_fitness

        Helper.show_plot(generations, generations_max_fitness, x_label="generation", y_label="fitness", title="Evolutionary algorithm")

        return population.get_best_chromosome()

