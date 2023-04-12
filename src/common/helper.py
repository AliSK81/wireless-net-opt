from random import randint


class Helper:
    def __init__(self):
        """
        Constructor for Helper class.
        """
        pass

    def read_blocks_population(self, file: str) -> list:
        """
        Reads the blocks population data from file and returns as a matrix.

        Args:
            file (str): File containing the blocks population data.

        Returns:
            list: Matrix representing the blocks population data.
        """
        pass

    def read_problem_config(self, file: str) -> dict:
        """
        Reads the problem configuration data from file and returns as a dictionary.

        Args:
            file (str): File containing the problem configuration data.

        Returns:
            dict: Dictionary containing the problem configuration data.
        """
        pass

    def calculate_user_satisfaction(self, received_bandwidth: float, required_bandwidth: float) -> float:
        """
        Calculates user satisfaction based on received bandwidth and required bandwidth.

        Args:
            received_bandwidth (float): Received bandwidth in Mb/s.
            required_bandwidth (float): Required bandwidth in Mb/s.

        Returns:
            float: User satisfaction level.
        """
        pass

    def plot_fitness_graph(self, generation_fitness_list: list):
        """
        Plots the graph of changes in the average fitness of the population over generations.

        Args:
            generation_fitness_list (list): List of average fitness values for each generation.
        """
        pass

    @staticmethod
    def sort_two_points(two_points):
        """
        Sort the two points in ascending order.

        Args:
        - two_points (tuple): A tuple of two integers representing the two points.

        Returns:
        - tuple: A tuple of two integers representing the sorted points in ascending order.
        """
        return tuple(sorted(two_points))

    @staticmethod
    def create_two_rand_index(array):
        """
        Generate two random indices in the range [0, len(array)).

        Args:
        - array (list): A list for which two random indices need to be generated.

        Returns:
        - tuple: A tuple of two integers representing two random indices in the range [0, len(array)).
        """
        return randint(0, len(array)), randint(0, len(array))
