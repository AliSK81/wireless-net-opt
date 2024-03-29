from common.helper import Helper

BLOCKS_POPULATION_FILE = '../resources/blocks_population.txt'
PROBLEM_CONFIG_FILE = '../resources/problem_config.txt'
BLOCKS_POPULATION = Helper.read_blocks_population(BLOCKS_POPULATION_FILE)
PROBLEM_CONFIG = Helper.read_problem_config(PROBLEM_CONFIG_FILE)
CITIES_POPULATION = [col for row in BLOCKS_POPULATION for col in row]
CITIES_LOCATION = [(i, j) for i in range(len(BLOCKS_POPULATION)) for j in range(len(BLOCKS_POPULATION[0]))]
CITIES_COUNT = len(CITIES_LOCATION)
TOWER_CONSTRUCTION_COST = PROBLEM_CONFIG['tower_construction_cost']
TOWER_MAINTENANCE_COST = PROBLEM_CONFIG['tower_maintenance_cost']
USER_SATISFACTION_LEVELS = PROBLEM_CONFIG['user_satisfaction_levels']
USER_SATISFACTIONS_SCORES = PROBLEM_CONFIG['user_satisfaction_scores']
POPULATION_SIZE = 50
MAX_GENERATIONS = 200
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.1
LOCATION_MUTATION_STD = 1.0
BANDWIDTH_MUTATION_STD = 500.0
LOCATION_MIN_X = 0
LOCATION_MAX_X = len(BLOCKS_POPULATION)
LOCATION_MIN_Y = 0
LOCATION_MAX_Y = len(BLOCKS_POPULATION[0])
BANDWIDTH_MIN = 1
BANDWIDTH_MAX = 5000
TOWERS_MIN = 1
TOWERS_MAX = len(CITIES_LOCATION)
TOTAL_SATISFACTION_RATIO = 0.2
TOTAL_COST_RATIO = 0.1
EVOLUTION_TIMES = 10
