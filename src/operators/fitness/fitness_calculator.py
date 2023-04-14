from collections import defaultdict

import numpy as np

from common.config import *


class FitnessCalculator:
    def __init__(self, tower_construction_cost=TOWER_CONSTRUCTION_COST,
                 tower_maintenance_cost=TOWER_MAINTENANCE_COST,
                 user_satisfaction_levels=USER_SATISFACTION_LEVELS,
                 user_satisfaction_scores=USER_SATISFACTIONS_SCORES,
                 cities_location=CITIES_LOCATION,
                 cities_population=CITIES_POPULATION,
                 total_satisfaction_ratio=TOTAL_SATISFACTION_RATIO,
                 total_cost_ratio=TOTAL_COST_RATIO):
        """
        Constructor method for the FitnessCalculator class.

        Initializes the following instance variables:
            - sigma: The covariance matrix used to calculate the coverage of a tower.
            - sigma_inv: The inverse of the covariance matrix.
            - tower_construction_cost: The cost of constructing a new tower.
            - tower_maintenance_cost: The cost of maintaining a tower per unit of bandwidth.
            - user_satisfaction_levels: The levels of user satisfaction for different levels of bandwidth.
            - user_satisfaction_scores: The satisfaction scores corresponding to each user satisfaction level.
            - cities_location: The location of each city as a tuple of (latitude, longitude).
            - cities_population: The population of each city.
            - total_satisfaction_ratio: The ratio by which the total user satisfaction should be multiplied in
                                         the final fitness calculation.
            - total_cost_ratio: The ratio by which the total cost should be multiplied in the final fitness
                                 calculation.
        """
        self.sigma = np.array([[8, 0], [0, 8]])
        self.sigma_inv = np.linalg.inv(self.sigma)
        self.tower_construction_cost = tower_construction_cost
        self.tower_maintenance_cost = tower_maintenance_cost
        self.user_satisfaction_levels = user_satisfaction_levels
        self.user_satisfaction_scores = user_satisfaction_scores
        self.cities_location = cities_location
        self.cities_population = cities_population
        self.total_satisfaction_ratio = total_satisfaction_ratio
        self.total_cost_ratio = total_cost_ratio

    @staticmethod
    def calc_bw_prime(tower_bandwidth, city_population, associated_cities_population):
        """
        Calculates the bandwidth allocated to a city based on the bandwidth of the tower it is connected to, the
         population of the city,
        and the total population of all cities connected to that tower.

        Args:
            tower_bandwidth (float): the bandwidth of the tower
            city_population (float): the population of the city
            associated_cities_population (float): the total population of all cities connected to the same tower as the
             city

        Returns:
            float: the bandwidth allocated to the city
        """
        return city_population / associated_cities_population * tower_bandwidth

    def calc_coverage(self, tower_location, city_location):
        """
        Calculates the coverage of a tower on a specific city location.

        Parameters:
        tower_location (tuple): The (x, y) location of the tower.
        city_location (tuple): The (x, y) location of the city.

        Returns:
        float: The coverage of the tower on the city location.
        """
        diff = np.array(city_location) - np.array(tower_location)
        diff_t = diff.T
        exp_term = -0.5 * diff @ self.sigma_inv @ diff_t
        covariance = np.exp(exp_term)
        return covariance

    def calc_bandwidth(self, tower, city_location, city_population, associated_cities_population):
        """
        Calculates the bandwidth for a given tower and city.

        Args:
            tower (Tower): The tower object representing the tower in question.
            city_location (tuple): A tuple representing the (x,y) location of the city.
            city_population (float): The population of the city in question.
            associated_cities_population (float): The total population of all cities associated with the given tower.

        Returns:
            float: The bandwidth available for the city.

        """
        coverage = self.calc_coverage(tower.location, city_location)
        bw_prime = self.calc_bw_prime(tower.bandwidth, city_population, associated_cities_population)
        return coverage * bw_prime

    def calc_city_satisfaction_score(self, city_bandwidth, city_population):
        user_satisfaction_level = city_bandwidth / city_population

        if user_satisfaction_level < self.user_satisfaction_levels[0]:
            return 0

        for i in range(len(self.user_satisfaction_levels)):
            if user_satisfaction_level < self.user_satisfaction_levels[i]:
                return self.user_satisfaction_scores[i - 1] * city_population
        return self.user_satisfaction_scores[-1] * city_population

    @staticmethod
    def group_by(genes):
        """
        Group cities by the tower they are connected to.

        Args:
        - genes (list): A list of integers representing the tower index for each city.

        Returns:
        - groups (defaultdict(list)): A dictionary where the keys are the unique tower indices
                                       and the values are the list of city indices connected to that tower.
        """
        groups = defaultdict(list)
        for city_index, tower in enumerate(genes):
            groups[tower].append(city_index)
        return groups

    def calc_total_cost(self, genes):
        """
        Calculates the total cost of a solution with the given genes.

        Args:
            genes (list): A list of genes representing the solution to calculate the cost for.

        Returns:
            float: The total cost of the solution.

        """
        towers = set(genes)
        return self.tower_construction_cost * len(towers) + sum(
            [self.tower_maintenance_cost * tower.bandwidth for tower in towers])

    def calc_total_satisfaction(self, genes):
        """
        Calculates the total user satisfaction score for a given chromosome, where the satisfaction score is defined as
        the sum of user satisfaction scores of all cities.

        Args:
            genes (list): The genes of the chromosome that represent the towers to be placed in the cities.

        Returns:
            float: The total user satisfaction score of the chromosome.
        """
        cities_by_tower = self.group_by(genes)

        total_satisfaction = 0.0

        for city_index, tower in enumerate(genes):
            city_location = self.cities_location[city_index]
            city_population = self.cities_population[city_index]
            associated_cities_population = sum([self.cities_population[i] for i in cities_by_tower[tower]])
            city_bandwidth = self.calc_bandwidth(tower, city_location, city_population, associated_cities_population)
            city_satisfaction_score = self.calc_city_satisfaction_score(city_bandwidth, city_population)
            total_satisfaction += city_satisfaction_score * city_population

        return total_satisfaction

    def calculate_fitness(self, genes):
        """
        Calculates the fitness of a given set of genes.

        The fitness is calculated as the total satisfaction of all users divided by the total cost of tower construction
        and maintenance. The higher the fitness, the better the set of genes.

        Args:
            genes (list): A list of integers representing the index of the tower assigned to each city.

        Returns:
            float: The fitness score of the given set of genes.
        """
        total_cost = self.calc_total_cost(genes)
        total_satisfaction = self.calc_total_satisfaction(genes)
        return total_satisfaction / total_cost
