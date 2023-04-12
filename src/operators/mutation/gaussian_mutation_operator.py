import random


class GaussianMutationOperator:
    """
    A mutation operator that applies Gaussian mutation to a list of genes.
    """

    @staticmethod
    def mutate(genes: list, mutation_rate: float, mutation_std: float):
        """
        Mutates the genes by adding Gaussian-distributed random values to their location and bandwidth.

        Args:
            genes (list): List of genes to be mutated.
            mutation_rate (float): Probability of mutation for each gene.
            mutation_std (float): Standard deviation of the Gaussian distribution for mutation.

        Modifies:
            genes (list): Genes in the input list are modified by updating their location and bandwidth.

        Returns:
            list: List of mutated genes after applying Gaussian mutation.
        """

        for gene in genes:
            if random.random() < mutation_rate:
                mutation = random.gauss(0, mutation_std)
                gene.location = tuple(max(0, loc + mutation) for loc in gene.location)
                gene.bandwidth = max(0, gene.bandwidth + mutation)

        return genes
