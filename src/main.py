from core.algorithm import EvolutionaryAlgorithm
from common.config import *

if __name__ == '__main__':
    EvolutionaryAlgorithm(generation_count=MAX_GENERATIONS).run_evolve(3)
    print("finish")
