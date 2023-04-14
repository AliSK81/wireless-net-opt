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
        Initializes the genetic algorithm with the specified number of generations to evolve.

        Args:
            generation_count (int): The number of generations to evolve.

        Attributes:
            - generation_count (int): The number of generations to evolve.
            - generations (numpy.ndarray): An array containing the indices of each generation.
            - sum_of_avg_fitness (numpy.ndarray): An array containing the sum of the average fitness value for each
             generation.
            - min_of_avg_fitness (numpy.ndarray): An array containing the minimum average fitness value for each
             generation.
            - max_of_avg_fitness (numpy.ndarray): An array containing the maximum average fitness value for each
            generation.
        """

        self.generation_count = generation_count
        self.generations = np.arange(self.generation_count)
        self.sum_of_avg_fitness = np.zeros(generation_count, dtype=np.float64)
        self.min_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).max)
        self.max_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).min)

    def run_evolve(self, times: int = 1):
        """
        Runs the genetic algorithm for a given number of times and displays the results as a plot.

        Args:
            times (int): Number of times to run the genetic algorithm. Defaults to 1.
        Returns:
            None
        """
        for _ in range(times):
            str(self.__evolve())

        Helper.show_plot(x=self.generations, y=self.__get_avg_fitness(times),
                         y_min=self.min_of_avg_fitness, y_max=self.max_of_avg_fitness,
                         x_label="generation", y_label="fitness", title="Evolutionary algorithm")

    def __evolve(self):
        """
        Evolves the population for a certain number of generations or until a stopping criterion is met.

        Returns:
        - The best chromosome from the final generation.
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

            self.__update_avg_fitness(generation, population)

        return population.get_best_chromosome()

    def __update_avg_fitness(self, generation, population):
        """
        Update the statistics for average, maximum and minimum fitness for a given generation.

        Args:
            generation (int): The current generation.
            population (Population): The population whose fitness statistics will be updated.
        """
        average = sum([chromosome.fitness for chromosome in population.chromosomes]) / len(population.chromosomes)
        self.sum_of_avg_fitness[generation] += average
        self.max_of_avg_fitness[generation] = max(average, self.max_of_avg_fitness[generation])
        self.min_of_avg_fitness[generation] = min(average, self.min_of_avg_fitness[generation])

    def __get_avg_fitness(self, times):
        """
        Returns:
        - The average fitness of the population over generations.
        """
        return self.sum_of_avg_fitness / times

    def log(self, name, chromosomes):
        print(name + ':')
        print([len(set(ch.genes)) for ch in chromosomes])
        print()
