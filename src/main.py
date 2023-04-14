from common.config import *
from core.algorithm import EvolutionaryAlgorithm

if __name__ == '__main__':
    EvolutionaryAlgorithm(generation_count=MAX_GENERATIONS).run_evolve(5)
    print("finish")
