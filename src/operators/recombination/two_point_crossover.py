import random

from core.gene import Gene


class MultiPointsCrossoverOperator:

    def crossover(self, parent1: list['Gene'], parent2: list['Gene'], crossover_rate, num_points=None):
        """
        Performs multipoint crossover between two parent chromosomes.

        Args:
            parent1 (list): The first parent chromosome.
            parent2 (list): The second parent chromosome.
            crossover_rate (float, optional): The probability of performing crossover. Defaults to 0.8.
            num_points (int): The number of crossover points to be selected.

        Returns:
            tuple: A tuple containing the two child chromosomes.
        """
        if random.random() > crossover_rate:
            return self.copy(parent1), self.copy(parent2)

        if num_points is None:
            num_points = random.randint(1, len(parent1))

        crossover_points = sorted(random.sample(range(len(parent1)), num_points))

        child1 = []
        child2 = []

        for i in range(len(parent1)):
            if i not in crossover_points:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])

        return self.copy(child1), self.copy(child2)

    @staticmethod
    def copy(child):
        child_copy = [None] * len(child)
        child_indices = {}
        for i, ch in enumerate(child):
            if ch not in child_indices.keys():
                new_tower = ch.copy()
                child_copy[i] = new_tower
                child_indices[ch] = new_tower
            else:
                child_copy[i] = child_indices[ch]
        return child_copy
