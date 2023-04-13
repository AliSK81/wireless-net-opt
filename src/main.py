from core.algorithm import EvolutionaryAlgorithm
from common.config import *

if __name__ == '__main__':
    EvolutionaryAlgorithm().evolve(generations=MAX_GENERATIONS)
    print("finish")
