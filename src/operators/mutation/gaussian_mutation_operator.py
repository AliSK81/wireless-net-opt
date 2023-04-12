import random


class GaussianMutationOperator:

    @staticmethod
    def mutate(genes, mutate_rate, stddev):
        mutated_genes = []
        for gene in genes:
            if random.random() < mutate_rate:
                mutation = random.gauss(0, stddev)
                mutated_gene = gene + mutation
                mutated_genes.append(mutated_gene)
            else:
                mutated_genes.append(gene)
        return mutated_genes
