import random

from core.chromosome import Chromosome
from common.config import *


class Population:
    def __init__(self, chromosomes=None):
        """
        Initialize a population with a given list of chromosomes.

        Args:
        - chromosomes (list): List of chromosomes representing the initial population.
        """
        self.chromosomes = chromosomes or []

    @staticmethod
    def initialize():
        """
        Generate random chromosomes for the population.

        Args:
        - size (int): The size of the population to generate.

        Modifies:
        - self.chromosomes (list): List of chromosomes in the population with randomly generated values.

        Returns:
        - chromosomes (list): List of chromosomes in the population.
        """
        population = Population()

        population.chromosomes = []
        for _ in range(POPULATION_SIZE):
            chromosome = Chromosome.initialize()
            population.chromosomes.append(chromosome)

        return population

    def fitness_proportionate_selection(self, num_parents):
        total_fitness = sum([chromosome.fitness for chromosome in self.chromosomes])

        probabilities = [chromosome.fitness / total_fitness for chromosome in self.chromosomes]

        parents = []
        for i in range(num_parents):
            parent = random.choices(self.chromosomes, weights=probabilities)[0]
            parents.append(parent)

        return parents

    def select_chromosomes(self) -> list:
        parents = self.fitness_proportionate_selection(num_parents=POPULATION_SIZE)

        return parents

    def crossover(self, crossover_rate):
        """
        Apply the crossover operator to generate offspring chromosomes.

        Returns:
        - offspring_chromosomes (list): List of offspring chromosomes generated from crossover.
        """

        offspring_chromosomes = []

        for parent1, parent2 in self.__random_pairing(self.chromosomes):
            offspring1, offspring2 = parent1.crossover(parent2, crossover_rate)
            offspring_chromosomes += [offspring1, offspring2]

        return Population(chromosomes=offspring_chromosomes)

    @staticmethod
    def __random_pairing(chromosomes):
        """
        Randomly pairs up chromosomes for crossover.

        Args:
            chromosomes (list): List of chromosomes to be paired up.

        Returns:
            list: List of pairs of chromosomes for crossover.
        """
        chromosomes = chromosomes[:]
        # random.shuffle(chromosomes)

        pairs = [(chromosomes[i], chromosomes[i + 1]) for i in range(0, len(chromosomes), 2)]

        if len(chromosomes) % 2 != 0:
            pairs[-1] = (chromosomes[-1], chromosomes[-1])

        return pairs

    def mutate(self, mutation_rate: float) -> None:
        """
        Apply the mutation operator to introduce small changes in the chromosomes.

        Args:
        - mutation_rate (float): The mutation rate, which determines the probability of each gene in a chromosome
                              being mutated.

        Returns:
        - None: This method mutates the chromosomes in-place and does not return any value.
        """
        for chromosome in self.chromosomes:
            chromosome.mutate(mutation_rate)

    def evaluate_fitness(self):
        """
        Evaluate the fitness of each chromosome in the population.

        Args:
        - chromosomes (list): List of chromosomes to be evaluated for fitness.

        Modifies:
        - Updates the fitness values of the chromosomes in the population.
        """
        for chromosome in self.chromosomes:
            chromosome.calculate_fitness()

    def replace(self, other: 'Population'):
        """
        Replace the least fit chromosomes with offspring chromosomes to create a new generation.

        Args:
        - offspring_chromosomes (list): List of offspring chromosomes to replace the least fit individuals.

        Modifies:
        - Updates the population with the offspring chromosomes, replacing the least fit individuals.
        """
        combined_chromosomes = self.chromosomes + other.chromosomes
        sorted_chromosomes = sorted(combined_chromosomes, key=lambda chromosome: chromosome.fitness, reverse=True)
        self.chromosomes = sorted_chromosomes[:len(self.chromosomes)]

    def get_best_chromosome(self):
        max(self.chromosomes, key=lambda chromosome: chromosome.fitness)
