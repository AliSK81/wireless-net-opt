import random
from common.helper import Helper


class TwoPointsCrossoverOperator:

    @staticmethod
    def crossover(parent1, parent2, crossover_rate):
        """
        Performs two-point crossover between two parent chromosomes.

        Args:
            parent1 (list): The first parent chromosome.
            parent2 (list): The second parent chromosome.
            crossover_rate (float, optional): The probability of performing crossover. Defaults to 0.8.

        Returns:
            tuple: A tuple containing the two child chromosomes.
        """
        if random.random() > crossover_rate:
            return parent1[:], parent2[:]

        parent1_point1, parent1_point2 = Helper.create_two_rand_index(parent1)
        parent2_point1, parent2_point2 = Helper.create_two_rand_index(parent2)

        child1 = parent1[:parent1_point1] + parent2[parent2_point1:parent2_point2] + parent1[parent1_point2:]
        child2 = parent2[:parent2_point1] + parent1[parent1_point1:parent1_point2] + parent2[parent2_point2:]

        return child1, child2