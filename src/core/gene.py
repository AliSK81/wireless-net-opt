import random


class Gene:
    def __init__(self, location: tuple = None, bandwidth: float = None):
        self.location = location
        self.bandwidth = bandwidth

    @staticmethod
    def initialize():
        gene = Gene()

        gene.location = (random.uniform(-10, 10), random.uniform(-10, 10))
        gene.bandwidth = random.uniform(0, 1)

        return gene
