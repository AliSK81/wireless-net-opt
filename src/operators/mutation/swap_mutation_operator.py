import random


class SwapMutationOperator:

    @staticmethod
    def mutate(genes, mutate_rate):
        mutated_genes = genes[:]

        if random.random() > mutate_rate:
            return mutated_genes

        i = random.randint(0, len(mutated_genes) - 1)
        j = random.randint(0, len(mutated_genes) - 1)
        mutated_genes[i], mutated_genes[j] = mutated_genes[j], mutated_genes[i]

        return genes
