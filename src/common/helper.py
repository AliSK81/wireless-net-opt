import json
from random import randint


class Helper:
    def __init__(self):
        """
        Constructor for Helper class.
        """
        pass

    @staticmethod
    def read_blocks_population(path: str) -> list:
        """
        Reads the blocks population data from file and returns as a matrix.

        Args:
            path (str): File containing the blocks population data.

        Returns:
            list: Matrix representing the blocks population data.
        """
        with open(path, 'r') as file:
            matrix = [list(map(int, line.strip().split(','))) for line in file]
        return matrix

    @staticmethod
    def read_problem_config(path: str) -> dict:
        """
        Reads the problem configuration data from file and returns as a dictionary.

        Args:
            path (str): File containing the problem configuration data.

        Returns:
            dict: Dictionary containing the problem configuration data.
        """
        with open(path, 'r') as file:
            config = json.load(file)
        return config

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
