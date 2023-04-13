import random
from random import randint

from core.gene import Gene
from operators.fitness.fitness_calculator import FitnessCalculator
from operators.mutation.gaussian_mutation_operator import GaussianMutationOperator
from operators.mutation.swap_mutation_operator import SwapMutationOperator

from common.helper import Helper
from operators.recombination.two_point_crossover import TwoPointsCrossoverOperator
from common.config import *


class Chromosome:
    def __init__(self, genes=None):
        """
        Initialize an empty chromosome with allocations, locations, and band widths for each tower.

        Attributes:
        - allocations (list): A list representing the allocation of towers to the cities.
                              The index of the list corresponds to the city number,
                              and the value at that index corresponds to the tower number assigned to that city.
        - locations (list): A list representing the locations of each tower.
        - band_widths (list): A list representing the bandwidths of each tower.
        """
        self.genes = genes or []
        self.fitness = None

    @staticmethod
    def initialize():
        chromosome = Chromosome()

        tower_count = randint(TOWERS_MIN, TOWERS_MAX)
        towers = [Gene.initialize() for _ in range(tower_count)]

        chromosome.genes = [random.choice(towers) for _ in range(CITIES_COUNT)]
        chromosome.fitness = chromosome.calculate_fitness()

        return chromosome

    def crossover(self, other, crossover_rate):
        """
        Perform crossover with another chromosome and generate offspring chromosome.

        Args:
        - other (Chromosome): Another chromosome to perform crossover with.
        - crossover_rate (float): The probability of performing crossover between the parents.

        Returns:
        - offspring (Tuple[Chromosome, Chromosome]): A tuple containing two offspring chromosomes generated from the crossover.
        """

        offspring1_genes, offspring2_genes = TwoPointsCrossoverOperator.crossover(self.genes, other.genes,
                                                                                  crossover_rate)

        offspring1 = Chromosome(offspring1_genes)
        offspring2 = Chromosome(offspring2_genes)

        return offspring1, offspring2

    def mutate(self, mutation_rate: float) -> None:
        """
        Perform mutation on the chromosome's genes.

        Args:
        - mutation_rate (float): The probability of mutation for each gene.

        Returns:
        None
        """
        self.genes = GaussianMutationOperator.mutate(genes=self.genes, mutation_rate=mutation_rate, mutation_std=0.01)
        self.genes = SwapMutationOperator.mutate(genes=self.genes, mutation_rate=mutation_rate)

    def calculate_fitness(self) -> float:
        """
        Calculate the fitness value of the chromosome based on the objective function.

        Returns:
        - float: The fitness value of the chromosome.
        """
        self.fitness = FitnessCalculator.calculate_fitness(self.genes)
        return self.fitness
