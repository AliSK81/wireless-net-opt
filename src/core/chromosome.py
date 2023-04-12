import random
from random import randint

from core.gene import Gene
from operators.mutation.gaussian_mutation_operator import GaussianMutationOperator
from operators.mutation.swap_mutation_operator import SwapMutationOperator

from common.helper import Helper
from operators.recombination.two_point_crossover import TwoPointsCrossoverOperator


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

    @staticmethod
    def initialize(gene_size: int):
        chromosome = Chromosome()

        tower_sizes = randint(0, gene_size // 2)
        towers = [Gene.initialize() for _ in range(tower_sizes)]

        chromosome.genes = [random.choice(towers) for _ in range(gene_size)]

        return chromosome

    def generate_random_genes(self) -> None:
        """
        Generate random allocations, locations, and band widths for the chromosome.

        Modifies:
        - self.allocations: The list representing the allocations of the chromosome.
        - self.locations: The list representing the locations of the chromosome.
        - self.bandwidths: The list representing the band widths of the chromosome.
        """
        pass

    def crossover(self, other, crossover_rate):
        """
        Perform crossover with another chromosome and generate offspring chromosome.

        Args:
        - other (Chromosome): Another chromosome to perform crossover with.
        - crossover_rate (float): The probability of performing crossover between the parents.

        Returns:
        - offspring (Tuple[Chromosome, Chromosome]): A tuple containing two offspring chromosomes generated from the crossover.
        """

        offspring1_genes, offspring2_genes = TwoPointsCrossoverOperator.crossover(self.genes, other.genes, crossover_rate)

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
        self.genes = GaussianMutationOperator.mutate(genes=self.genes, mutation_rate=mutation_rate, mutation_std=1)
        self.genes = SwapMutationOperator.mutate(genes=self.genes, mutation_rate=mutation_rate)

    def calculate_fitness(self) -> float:
        """
        Calculate the fitness value of the chromosome based on the objective function.

        Returns:
        - float: The fitness value of the chromosome.
        """
        pass
