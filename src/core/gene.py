import random

from common.config import *


class Gene:
    def __init__(self, location: tuple = None, bandwidth: float = None):
        self.location = location
        self.bandwidth = bandwidth

    @staticmethod
    def initialize():
        gene = Gene()

        gene.location = (random.uniform(LOCATION_MIN_X, LOCATION_MAX_X), random.uniform(LOCATION_MIN_Y, LOCATION_MAX_Y))
        gene.bandwidth = random.uniform(BANDWIDTH_MIN, BANDWIDTH_MAX)

        return gene

    def copy(self):
        return Gene(self.location, self.bandwidth)
