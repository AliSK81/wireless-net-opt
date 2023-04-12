import random


class GaussianMutationOperator:
    def __init__(self, mutation_rate, stddev):
        self.mutation_rate = mutation_rate
        self.stddev = stddev

    def mutate(self, genes):
        mutated_genes = []
        for gene in genes:
            if random.random() < self.mutation_rate:
                mutation = random.gauss(0, self.stddev)
                mutated_gene = gene + mutation
                mutated_genes.append(mutated_gene)
            else:
                mutated_genes.append(gene)
        return mutated_genes
