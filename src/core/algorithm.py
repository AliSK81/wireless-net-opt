import time

from core.population import Population
from common.config import *


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

    def evolve(self, generations: int):
        """
        Evolves the population for a certain number of generations or until a stopping criterion is met.

        Args:
            generations (int): Number of generations to evolve.
            stopping_criterion (float): Stopping criterion for terminating the evolution process.

        Returns:
            None
        """
        population = Population.initialize()
        population.evaluate_fitness()

        for generation in range(generations):
            # print("selected_chromosomes")
            # selected_chromosomes = population.select_chromosomes()
            # print([len(set(ch.genes)) for ch in selected_chromosomes])
            # print()
            new_generation = Population(population.chromosomes[:])

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
            print(max(population.chromosomes, key=lambda x: x.fitness).fitness)

        return population.get_best_chromosome()
