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
        return city_population / associated_cities_population * tower_bandwidth

    def calc_coverage(self, tower_location, city_location):
        diff = np.array(city_location) - np.array(tower_location)
        diff_t = diff.T
        exp_term = -0.5 * diff @ self.sigma_inv @ diff_t
        covariance = np.exp(exp_term)
        return covariance

    def calc_bandwidth(self, tower, city_location, city_population, associated_cities_population):
        coverage = self.calc_coverage(tower.location, city_location)
        bw_prime = self.calc_bw_prime(tower.bandwidth, city_population, associated_cities_population)
        return coverage * bw_prime

    def calc_user_satisfaction_score(self, city_bandwidth, city_population):
        user_satisfaction_level = city_bandwidth / city_population

        if user_satisfaction_level < self.user_satisfaction_levels[0]:
            return 0

        for i in range(len(self.user_satisfaction_levels)):
            if user_satisfaction_level < self.user_satisfaction_levels[i]:
                return self.user_satisfaction_scores[i - 1]
        return self.user_satisfaction_scores[-1]

    @staticmethod
    def group_by(genes):
        groups = defaultdict(list)
        for city_index, tower in enumerate(genes):
            groups[tower].append(city_index)
        return groups

    def calc_total_cost(self, genes):
        towers = set(genes)
        return self.tower_construction_cost * len(towers) + sum(
            [self.tower_maintenance_cost * tower.bandwidth for tower in towers])

    def calc_total_satisfaction(self, genes):
        cities_by_tower = self.group_by(genes)

        total_satisfaction = 0.0

        for city_index, tower in enumerate(genes):
            city_location = self.cities_location[city_index]
            city_population = self.cities_population[city_index]
            associated_cities_population = sum([self.cities_population[i] for i in cities_by_tower[tower]])
            city_bandwidth = self.calc_bandwidth(tower, city_location, city_population, associated_cities_population)
            user_satisfaction_score = self.calc_user_satisfaction_score(city_bandwidth, city_population)
            total_satisfaction += user_satisfaction_score * city_population

        return total_satisfaction

    def calculate_fitness(self, genes):
        total_cost = self.calc_total_cost(genes)
        total_satisfaction = self.calc_total_satisfaction(genes)
        return self.total_satisfaction_ratio * total_satisfaction - self.total_cost_ratio * total_cost
