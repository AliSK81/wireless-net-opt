import random


class FitnessProportionateOperator:

    def __init__(self):
        pass

    def select(self, chromosomes, num_parents):
        total_fitness = sum([chromosome.fitness for chromosome in chromosomes])

        probabilities = [chromosome.fitness / total_fitness for chromosome in chromosomes]

        parents = []
        for i in range(num_parents):
            parent = random.choices(chromosomes, weights=probabilities)[-1]
            parents.append(parent)

        return parents
