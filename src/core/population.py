import random
from random import randint

from core.chromosome import Chromosome


class Population:
    def __init__(self, chromosomes=None):
        """
        Initialize a population with a given list of chromosomes.

        Args:
        - chromosomes (list): List of chromosomes representing the initial population.
        """
        self.chromosomes = chromosomes or []

    def initialize(self, size: int):
        """
        Generate random chromosomes for the population.

        Args:
        - size (int): The size of the population to generate.

        Modifies:
        - self.chromosomes (list): List of chromosomes in the population with randomly generated values.

        Returns:
        - chromosomes (list): List of chromosomes in the population.
        """
        self.chromosomes = []
        for i in range(size):
            chromosome = Chromosome()
            self.chromosomes.append(chromosome)
        return self.chromosomes

    def select_chromosomes(self) -> list:
        """
        Select chromosomes for reproduction using tournament selection or roulette wheel selection.

        Returns:
        - selected_chromosomes (list): List of selected chromosomes from the current population.
        """
        pass

    def crossover(self) -> list:
        """
        Apply the crossover operator to generate offspring chromosomes.

        Returns:
        - offspring_chromosomes (list): List of offspring chromosomes generated from crossover.
        """
        offspring = []

        for parent1, parent2 in self.__random_pairing(self.chromosomes):
            offspring1, offspring2 = parent1.crossover(parent2)
            offspring.extend([offspring1, offspring])

        return offspring

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
        random.shuffle(chromosomes)

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

    def evaluate_fitness(self, chromosomes: list):
        """
        Evaluate the fitness of each chromosome in the population.

        Args:
        - chromosomes (list): List of chromosomes to be evaluated for fitness.

        Modifies:
        - Updates the fitness values of the chromosomes in the population.
        """
        pass

    def replace(self, offspring_chromosomes: list):
        """
        Replace the least fit chromosomes with offspring chromosomes to create a new generation.

        Args:
        - offspring_chromosomes (list): List of offspring chromosomes to replace the least fit individuals.

        Modifies:
        - Updates the population with the offspring chromosomes, replacing the least fit individuals.
        """
        pass
