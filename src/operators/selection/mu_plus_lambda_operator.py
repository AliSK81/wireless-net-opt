class MuPlusLambdaOperator:

    def select(self, parents, offsprings):
        combined_chromosomes = parents + offsprings
        sorted_chromosomes = sorted(combined_chromosomes, key=lambda chromosome: chromosome.fitness, reverse=True)
        return sorted_chromosomes[:len(parents)]
