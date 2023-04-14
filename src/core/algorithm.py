import numpy as np

from common.config import *
from core.chromosome import Chromosome
from core.population import Population
from operators.fitness.fitness_calculator import FitnessCalculator


class EvolutionaryAlgorithm:
    """
    Represents an evolutionary algorithm for solving the problem of determining the optimal number of telecommunication
    towers, their location coordinates, and the bandwidth required for each tower, while considering the initial
    construction cost and maintenance cost based on the bandwidth.
    """

    def __init__(self, generation_count: int):
        """
        Initializes the genetic algorithm with the specified number of generations to evolve.

        Args:
            generation_count (int): The number of generations to evolve.

        Attributes:
            - generation_count (int): The number of generations to evolve.
            - generations (numpy.ndarray): An array containing the indices of each generation.
            - sum_of_avg_fitness (numpy.ndarray): An array containing the sum of the average fitness value for each
             generation.
            - min_of_avg_fitness (numpy.ndarray): An array containing the minimum average fitness value for each
             generation.
            - max_of_avg_fitness (numpy.ndarray): An array containing the maximum average fitness value for each
            generation.
        """

        self.generation_count = generation_count
        self.generations = np.arange(self.generation_count)
        self.sum_of_avg_fitness = np.zeros(generation_count, dtype=np.float64)
        self.min_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).max)
        self.max_of_avg_fitness = np.full(generation_count, np.finfo(np.float64).min)

    def run_evolve(self, times: int = 1):
        for _ in range(times):
            best_sol = self.__evolve()
            Helper.write_dict_to_json(self.__get_best_solution_info(best_sol))

        Helper.show_plot(x=self.generations, y=self.__get_average_of_avg_fitness(times),
                         y_min=self.min_of_avg_fitness, y_max=self.max_of_avg_fitness,
                         x_label="generation", y_label="fitness", title="Evolutionary algorithm")

    def __evolve(self):
        """
        Evolves the population for a certain number of generations or until a stopping criterion is met.

        Returns:
        - The best chromosome from the final generation.
        """
        population = Population.initialize()
        population.evaluate_fitness()

        for generation in range(self.generation_count):
            selected_chromosomes = population.select_chromosomes()

            new_generation = Population(selected_chromosomes)

            new_generation = new_generation.crossover(CROSSOVER_RATE)

            new_generation.mutate(MUTATION_RATE)

            new_generation.evaluate_fitness()

            population.replace(new_generation)

            self.__print_max_fitness(population)

            self.__update_avg_fitness(generation, population)

        return population.get_best_chromosome()

    def __print_max_fitness(self, population):
        max_fitness = max(population.chromosomes, key=lambda x: x.fitness).fitness
        print(max_fitness)

    def __update_avg_fitness(self, generation, population):
        average = sum([chromosome.fitness for chromosome in population.chromosomes]) / len(population.chromosomes)
        self.sum_of_avg_fitness[generation] += average
        self.max_of_avg_fitness[generation] = max(average, self.max_of_avg_fitness[generation])
        self.min_of_avg_fitness[generation] = min(average, self.min_of_avg_fitness[generation])

    @staticmethod
    def __get_best_solution_info(chromosome: 'Chromosome'):
        fitness_calc = FitnessCalculator()
        allocations = fitness_calc.group_by(chromosome.genes)

        fitness = fitness_calc.calculate_fitness(chromosome.genes)
        total_cost = fitness_calc.calc_total_cost(chromosome.genes)
        total_satisfaction = fitness_calc.calc_total_satisfaction(chromosome.genes)
        num_of_towers = len(set(chromosome.genes))

        towers = []
        for tower, cities in allocations.items():
            tower_info = {
                'loc': tower.location,
                'bw': tower.bandwidth,
                'cities': []
            }
            for city_num in cities:
                city_location = CITIES_LOCATION[city_num]
                city_population = CITIES_POPULATION[city_num]
                total_population = sum([CITIES_POPULATION[c] for c in cities])
                bandwidth = fitness_calc.calc_bandwidth(tower, city_location, city_population, total_population)
                city_satisfaction = fitness_calc.calc_city_satisfaction_score(bandwidth, city_population)
                city_info = {
                    'location': city_location,
                    'population': city_population,
                    'bw': bandwidth,
                    'satisfaction': city_satisfaction
                }
                tower_info['cities'].append({city_num: city_info})
            towers.append(tower_info)

        return {
            'fitness': fitness,
            'total_cost': total_cost,
            'total_satisfaction': total_satisfaction,
            'num_of_towers': num_of_towers,
            'towers': towers
        }

    def __get_average_of_avg_fitness(self, times):
        return self.sum_of_avg_fitness / times
