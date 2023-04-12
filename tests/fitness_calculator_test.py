import unittest

from core.gene import Gene
from operators.fitness.fitness_calculator import FitnessCalculator


class TestFitnessCalculator(unittest.TestCase):
    def test_calculate_fitness(self):
        gene1 = Gene(location=(1, 2), bandwidth=10)
        gene2 = Gene(location=(3, 4), bandwidth=30)
        gene3 = gene1
        genes = [gene1, gene2, gene3]

        fitness = FitnessCalculator.calculate_fitness(genes)
        expected_fitness = 17620

        self.assertEqual(fitness, expected_fitness)


if __name__ == '__main__':
    unittest.main()
