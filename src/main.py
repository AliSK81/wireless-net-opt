from common.config import *
from core.algorithm import EvolutionaryAlgorithm
import time

if __name__ == '__main__':
    start_time = time.time()

    EvolutionaryAlgorithm(generation_count=MAX_GENERATIONS).run_evolve(EVOLUTION_TIMES)

    end_time = time.time()
    runtime = end_time - start_time
    print("\nRuntime: {} seconds".format(runtime))
