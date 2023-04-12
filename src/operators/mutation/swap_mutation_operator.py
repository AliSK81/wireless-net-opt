import random


class SwapMutationOperator:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def mutate(self, genes):
        mutated_genes = genes[:]

        if random.random() > self.mutation_rate:
            return mutated_genes

        i = random.randint(0, len(mutated_genes) - 1)
        j = random.randint(0, len(mutated_genes) - 1)
        mutated_genes[i], mutated_genes[j] = mutated_genes[j], mutated_genes[i]

        return genes
