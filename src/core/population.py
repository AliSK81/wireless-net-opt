class Population:
    def __init__(self, size: int):
        """
        Initialize a population with a given size.

        Args:
        - size (int): Size of the population.
        """
        pass

    def initialize(self):
        """
        Generate random chromosomes for the population.

        Modifies:
        - self.chromosomes: List of chromosomes in the population with randomly generated values.
        """
        pass

    def select_chromosomes(self) -> list:
        """
        Select chromosomes for reproduction using tournament selection or roulette wheel selection.

        Returns:
        - selected_chromosomes (list): List of selected chromosomes from the current population.
        """
        pass

    def crossover(self, chromosomes: list) -> list:
        """
        Apply the crossover operator to generate offspring chromosomes.

        Args:
        - chromosomes (list): List of chromosomes to be used for crossover.

        Returns:
        - offspring_chromosomes (list): List of offspring chromosomes generated from crossover.
        """
        pass

    def mutate(self, chromosomes: list) -> list:
        """
        Apply the mutation operator to introduce small changes in offspring chromosomes.

        Args:
        - chromosomes (list): List of chromosomes to be used for mutation.

        Returns:
        - mutated_chromosomes (list): List of offspring chromosomes generated from mutation.
        """
        pass

    def evaluate_fitness(self, chromosomes: list):
        """
        Evaluate the fitness of each chromosome in the population.

        Args:
        - chromosomes (list): List of chromosomes to be evaluated for fitness.

        Modifies:
        - Updates the fitness values of the chromosomes in the population.
        """
        pass

    def replace(self, offspring_chromosomes: list):
        """
        Replace the least fit chromosomes with offspring chromosomes to create a new generation.

        Args:
        - offspring_chromosomes (list): List of offspring chromosomes to replace the least fit individuals.

        Modifies:
        - Updates the population with the offspring chromosomes, replacing the least fit individuals.
        """
        pass
