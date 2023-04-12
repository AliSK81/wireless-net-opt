import random


class SwapMutationOperator:
    """
    A mutation operator that performs swap mutation on a list of genes.
    """

    @staticmethod
    def mutate(genes, mutation_rate):
        """
        Performs swap mutation on a list of genes.

        Args:
            genes (list): List of genes to be mutated.
            mutation_rate (float): Probability of mutation for each gene.

        Modifies:
            genes (list): Genes in the input list are modified by performing swap mutation.

        Returns:
            list: List of mutated genes after applying swap mutation.
        """
        if random.random() < mutation_rate:
            return genes

        i = random.randint(0, len(genes) - 1)
        j = random.randint(0, len(genes) - 1)
        genes[i], genes[j] = genes[j], genes[i]

        return genes
