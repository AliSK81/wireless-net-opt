import random


class FitnessProportionateOperator:

    def __init__(self, chromosomes):
        self._chromosomes = chromosomes

    def select(self, num_parents):
        total_fitness = sum([chromosome.fitness for chromosome in self._chromosomes])

        probabilities = [chromosome.fitness / total_fitness for chromosome in self._chromosomes]

        parents = []
        for i in range(num_parents):
            parent = random.choices(self._chromosomes, weights=probabilities)[0]
            parents.append(parent)

        return parents
