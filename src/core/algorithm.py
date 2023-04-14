import numpy as np

from common.config import *
from core.population import Population


class EvolutionaryAlgorithm:
    """
    Represents an evolutionary algorithm for solving the problem of determining the optimal number of telecommunication
    towers, their location coordinates, and the bandwidth required for each tower, while considering the initial
    construction cost and maintenance cost based on the bandwidth.
    """

    def __init__(self, generation_count: int):
        """
        Initializes the algorithm with input data from files.

        Args:
            generation_count (int): Number of generations to evolve.
        """

        self.generation_count = generation_count
        self.generations = np.arange(self.generation_count)
        self.sum_of_avg_fitness = np.zeros(generation_count, dtype=np.float64)
        self.min_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).max)
        self.max_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).min)

    def __evolve(self):
        """
        Evolves the population for a certain number of generations or until a stopping criterion is met.
        """
        population = Population.initialize()
        population.evaluate_fitness()

        for generation in range(self.generation_count):
            selected_chromosomes = population.select_chromosomes()

            new_generation = Population(selected_chromosomes)

            new_generation = new_generation.crossover(CROSSOVER_RATE)

            new_generation.mutate(MUTATION_RATE)

            new_generation.evaluate_fitness()

            population.replace(new_generation)

            max_fitness = max(population.chromosomes, key=lambda x: x.fitness).fitness
            print(max_fitness)

            average = sum([chromosome.fitness for chromosome in population.chromosomes]) / len(population.chromosomes)
            self.sum_of_avg_fitness[generation] += average
            self.max_of_avg_fitness[generation] = max(average, self.max_of_avg_fitness[generation])
            self.min_of_avg_fitness[generation] = min(average, self.min_of_avg_fitness[generation])

        return population.get_best_chromosome()

    def run_evolve(self, times: int = 1):
        for _ in range(times):
            self.__evolve()

        self.__show_plot(times)

    def __show_plot(self, times):
        average_of_avg_fitness = self.sum_of_avg_fitness / times

        Helper.show_plot(x=self.generations, y=average_of_avg_fitness,
                         y_min=self.min_of_avg_fitness, y_max=self.max_of_avg_fitness,
                         x_label="generation", y_label="fitness", title="Evolutionary algorithm")

    def log(self, name, chromosomes):
        print(name + ':')
        print([len(set(ch.genes)) for ch in chromosomes])
        print()
