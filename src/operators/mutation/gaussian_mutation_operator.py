import random

from common.config import *


class GaussianMutationOperator:
    """
    A mutation operator that applies Gaussian mutation to a list of genes.
    """

    def __init__(self,
                 location_min_x: float = LOCATION_MIN_X,
                 location_min_y: float = LOCATION_MIN_Y,
                 location_max_x: float = LOCATION_MAX_X,
                 location_max_y: float = LOCATION_MAX_Y,
                 bandwidth_min: float = BANDWIDTH_MIN,
                 bandwidth_max: float = BANDWIDTH_MAX):
        """
        Initializes the GaussianMutationOperator with config values.

        Args:
            location_min_x (float): Minimum value for x-axis location.
            location_min_y (float): Minimum value for y-axis location.
            location_max_x (float): Maximum value for x-axis location.
            location_max_y (float): Maximum value for y-axis location.
            bandwidth_min (float): Minimum value for bandwidth.
            bandwidth_max (float): Maximum value for bandwidth.
        """
        self.location_min_x = location_min_x
        self.location_min_y = location_min_y
        self.location_max_x = location_max_x
        self.location_max_y = location_max_y
        self.bandwidth_min = bandwidth_min
        self.bandwidth_max = bandwidth_max

    def mutate(self, genes: list,
               mutation_rate: float = MUTATION_RATE,
               location_mutation_std: float = LOCATION_MUTATION_STD,
               bandwidth_mutation_std: float = BANDWIDTH_MUTATION_STD):
        """
        Mutates the genes by adding Gaussian-distributed random values to their location and bandwidth separately.

        Args:
            genes (list): List of genes to be mutated.
            mutation_rate (float): Probability of mutation for each gene.
            location_mutation_std (float): Standard deviation of the Gaussian distribution for location mutation.
            bandwidth_mutation_std (float): Standard deviation of the Gaussian distribution for bandwidth mutation.

        Returns:
            list: List of mutated genes after applying Gaussian mutation.
        """

        for gene in genes:
            if random.random() < mutation_rate:
                location_mutation = random.gauss(0, location_mutation_std)
                bandwidth_mutation = random.gauss(0, bandwidth_mutation_std)

                gene.location = tuple(
                    max(self.location_min_x, min(self.location_max_x, loc + location_mutation))
                    for loc in gene.location)

                gene.bandwidth = max(self.bandwidth_min,
                                     min(self.bandwidth_max, gene.bandwidth + bandwidth_mutation))
