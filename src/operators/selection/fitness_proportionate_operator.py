import random


class FitnessProportionateOperator:

    @staticmethod
    def selection(self, num_parents):
        total_fitness = sum([chromosome.fitness for chromosome in self.chromosomes])

        probabilities = [chromosome.fitness / total_fitness for chromosome in self.chromosomes]

        parents = []
        for i in range(num_parents):
            parent = random.choices(self.chromosomes, weights=probabilities)[0]
            parents.append(parent)

        return parents
