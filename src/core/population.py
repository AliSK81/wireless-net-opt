from operators.selection.fitness_proportionate_operator import FitnessProportionateOperator
from operators.selection.mu_plus_lambda_operator import MuPlusLambdaOperator
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
        self.selection_operator = FitnessProportionateOperator()
        self.mu_plus_lambda_operator = MuPlusLambdaOperator()

    @staticmethod
    def initialize():
        """
        Static method that creates a new Population object with randomly initialized chromosomes.

        Returns:
            Population: A new Population object with randomly initialized chromosomes.
        """
        population = Population()

        population.chromosomes = []
        for _ in range(POPULATION_SIZE):
            chromosome = Chromosome.initialize()
            population.chromosomes.append(chromosome)

        return population

    def select_chromosomes(self) -> list:
        """
        Selects a list of chromosomes from the population using the selection operator.

        Returns:
            list: A list of selected Chromosome objects.
        """
        return self.selection_operator.select(self.chromosomes, POPULATION_SIZE)

    def crossover(self, crossover_rate):
        """
        Performs crossover between pairs of chromosomes in the population and returns a new population with the
         offspring.

        Args:
            crossover_rate (float): The probability that a crossover will occur between two parent chromosomes.

        Returns:
            Population: A new population object containing the offspring chromosomes created by crossover.
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
        self.chromosomes = self.mu_plus_lambda_operator.select(self.chromosomes, other.chromosomes)

    def get_best_chromosome(self):
        """
        Returns the best chromosome in the population based on fitness.

        Returns:
            Chromosome: The chromosome in the population with the highest fitness value.
        """
        return max(self.chromosomes, key=lambda chromosome: chromosome.fitness)
