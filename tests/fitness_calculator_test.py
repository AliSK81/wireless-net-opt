import unittest

from core.gene import Gene
from operators.fitness.fitness_calculator import FitnessCalculator


class TestFitnessCalculator(unittest.TestCase):
    def test_calculate_fitness(self):
        gene1 = Gene(location=(0.5, 0.75), bandwidth=10)
        gene2 = Gene(location=(0.4, 0.8), bandwidth=30)
        gene3 = gene1
        genes = [gene1, gene2, gene3]

        calculator = FitnessCalculator(
            tower_construction_cost=10,
            tower_maintenance_cost=10,
            user_satisfaction_levels=[10, 20, 30],
            user_satisfaction_scores=[100, 200, 300],
            cities_location=[(0, 0), (0, 10), (10, 0), (5, 5)],
            cities_population=[10, 20, 30, 40]
        )

        fitness = calculator.calculate_fitness(genes)
        expected_fitness = 59580000

        self.assertEqual(fitness, expected_fitness)


if __name__ == '__main__':
    unittest.main()
