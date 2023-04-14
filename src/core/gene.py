import random

from common.config import *


class Gene:
    def __init__(self, location: tuple = None, bandwidth: float = None):
        """
        Initializes a new Gene object with the given location and bandwidth.

        Args:
            location (tuple, optional): A tuple containing the x and y coordinates of the location of the gene. Defaults to None.
            bandwidth (float, optional): The bandwidth value of the gene. Defaults to None.
        """
        self.location = location
        self.bandwidth = bandwidth

    @staticmethod
    def initialize():
        """
        Static method that creates a new Gene object with randomly initialized location and bandwidth.

        Returns:
            Gene: A new Gene object with randomly initialized location and bandwidth.
        """
        gene = Gene()

        gene.location = (random.uniform(LOCATION_MIN_X, LOCATION_MAX_X), random.uniform(LOCATION_MIN_Y, LOCATION_MAX_Y))
        gene.bandwidth = random.uniform(BANDWIDTH_MIN, BANDWIDTH_MAX)

        return gene

    def copy(self):
        """
       Creates a copy of the current Gene object.

       Returns:
           Gene: A new Gene object with the same location and bandwidth as the current Gene object.
       """
        return Gene(self.location, self.bandwidth)

    def __str__(self):
        return f"Gene: location={self.location}, bandwidth={self.bandwidth}"