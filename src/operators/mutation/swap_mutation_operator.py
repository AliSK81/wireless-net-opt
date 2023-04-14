import random

from common.config import MUTATION_RATE


class SwapMutationOperator:
    """
    A mutation operator that performs swap mutation on a list of genes.
    """

    def mutate(self, genes, mutation_rate: float = MUTATION_RATE):
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

        for i in range(len(genes)):
            if random.random() < mutation_rate:
                j = random.randint(0, len(genes) - 1)
                genes[i], genes[j] = genes[j], genes[i]
