import random


class FitnessProportionateOperator:

    def __init__(self):
        pass

    def select(self, chromosomes, num_parents):
        """
        Selects parents from a list of chromosomes based on their fitness using the fitness proportionate selection algorithm.

        Args:
            chromosomes (list): List of Chromosome objects to select parents from.
            num_parents (int): The number of parents to select.

        Returns:
            list: List of selected parents.
        """
        total_fitness = sum([chromosome.fitness for chromosome in chromosomes])

        probabilities = [chromosome.fitness / total_fitness for chromosome in chromosomes]

        parents = []
        for i in range(num_parents):
            parent = random.choices(chromosomes, weights=probabilities)[-1]
            parents.append(parent)

        return parents
