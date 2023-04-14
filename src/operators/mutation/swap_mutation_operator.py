import random

from common.config import MUTATION_RATE


class SwapMutationOperator:
    """
    A mutation operator that performs swap mutation on a list of genes.
    """

    def mutate(self, genes, mutation_rate: float = MUTATION_RATE):
        """
        Mutates the given genes by swapping elements with a probability equal to the mutation_rate.

        Args:
        - genes: a list of integers representing the current tower assignment for each city
        - mutation_rate: a float representing the probability that a swap occurs between two elements in the genes list

        Returns:
        - None. The input genes list is modified in place.
        """
        for i in range(len(genes)):
            if random.random() < mutation_rate:
                j = random.randint(0, len(genes) - 1)
                genes[i], genes[j] = genes[j], genes[i]
