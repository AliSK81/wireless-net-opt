import random
from random import randint

from common.config import *
from core.gene import Gene
from operators.fitness.fitness_calculator import FitnessCalculator
from operators.mutation.gaussian_mutation_operator import GaussianMutationOperator
from operators.mutation.swap_mutation_operator import SwapMutationOperator
from operators.recombination.two_point_crossover import MultiPointsCrossoverOperator


class Chromosome:
    def __init__(self, genes=None):
        """
        Initialize a new Individual object with a list of genes.

        Args:
            genes (list): A list of genes representing the individual's genetic information. Defaults to an empty list
            if not provided.
        """
        self.genes = genes or []
        self.fitness = None
        self.fitness_calculator = FitnessCalculator()
        self.swap_mutation_operator = SwapMutationOperator()
        self.gaussian_mutation_operator = GaussianMutationOperator()
        self.multi_point_crossover_operator = MultiPointsCrossoverOperator()

    @staticmethod
    def initialize():
        """
       Static method that creates a new Chromosome object with randomly initialized genes.

       Returns:
           Chromosome: A new Chromosome object with randomly initialized genes.
        """
        chromosome = Chromosome()

        tower_count = randint(TOWERS_MIN, TOWERS_MAX)
        towers = [Gene.initialize() for _ in range(tower_count)]

        chromosome.genes = [random.choice(towers) for _ in range(CITIES_COUNT)]
        chromosome.fitness = chromosome.calculate_fitness()

        return chromosome

    def crossover(self, other, crossover_rate):
        """
        Performs crossover between two parent chromosomes to create two offspring chromosomes.

        Args:
            other (Chromosome): The other parent chromosome to cross with.
            crossover_rate (float): The probability of performing crossover.

        Returns:
            tuple: A tuple containing two new offspring Chromosome objects.
        """
        offspring1_genes, offspring2_genes = self.multi_point_crossover_operator.crossover(self.genes, other.genes,
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
        self.gaussian_mutation_operator.mutate(genes=self.genes, mutation_rate=mutation_rate)
        self.swap_mutation_operator.mutate(genes=self.genes, mutation_rate=mutation_rate)

    def calculate_fitness(self) -> float:
        """
        Calculate the fitness value of the chromosome based on the objective function.

        Returns:
        - float: The fitness value of the chromosome.
        """
        self.fitness = self.fitness_calculator.calculate_fitness(self.genes)
        return self.fitness

    def __str__(self):
        genes_str = ", \n".join(str(gene) for gene in self.genes)
        return f"Chromosome: genes=[\n{genes_str}\n],\nfitness={self.fitness}"
