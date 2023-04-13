import random
from collections import defaultdict

import numpy as np

from common.config import *


class FitnessCalculator:
    sigma = np.array([[8, 0], [0, 8]])
    sigma_inv = np.linalg.inv(sigma)

    @staticmethod
    def calc_bw_prime(tower_bandwidth, city_population, associated_cities_population):
        return city_population / associated_cities_population * tower_bandwidth

    @staticmethod
    def calc_coverage(tower_location, city_location):
        diff = np.array(city_location) - np.array(tower_location)
        diff_t = diff.T
        exp_term = -0.5 * diff @ FitnessCalculator.sigma_inv @ diff_t
        covariance = np.exp(exp_term)
        return covariance

    @staticmethod
    def calc_bandwidth(tower, city_location, city_population, associated_cities_population):
        coverage = FitnessCalculator.calc_coverage(tower.location, city_location)
        bw_prime = FitnessCalculator.calc_bw_prime(tower.bandwidth, city_population, associated_cities_population)
        return coverage * bw_prime

    @staticmethod
    def calc_user_satisfaction_level(city_bandwidth, city_population):
        return city_bandwidth / city_population

    @staticmethod
    def calc_user_satisfaction_score(user_satisfaction_level):
        for i in range(len(USER_SATISFACTION_LEVELS)):
            if user_satisfaction_level < USER_SATISFACTION_LEVELS[i]:
                return USER_SATISFACTIONS_SCORES[i]
        return USER_SATISFACTIONS_SCORES[-1]

    @staticmethod
    def group_by(genes):
        groups = defaultdict(list)

        for city_index, tower in enumerate(genes):
            groups[tower].append(city_index)

        return groups

    @staticmethod
    def calculate_fitness(genes):
        cities_by_tower = FitnessCalculator.group_by(genes)

        total_cost = sum([TOWER_CONSTRUCTION_COST + TOWER_MAINTENANCE_COST * tower.bandwidth for tower in set(genes)])
        total_satisfaction = 0.0

        for city_index, tower in enumerate(genes):
            city_location = CITIES_LOCATION[city_index]
            city_population = CITIES_POPULATION[city_index]
            associated_cities_population = sum([CITIES_POPULATION[i] for i in cities_by_tower[tower]])
            city_bandwidth = FitnessCalculator.calc_bandwidth(tower, city_location, city_population,
                                                              associated_cities_population)
            user_satisfaction_level = FitnessCalculator.calc_user_satisfaction_level(city_bandwidth, city_population)
            user_satisfaction_score = FitnessCalculator.calc_user_satisfaction_score(user_satisfaction_level)
            total_satisfaction += user_satisfaction_score * city_population

        return 10000*total_satisfaction - 1000*total_cost
