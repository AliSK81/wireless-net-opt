import json
import os
import time
from random import randint

from matplotlib import pyplot as plt


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
    def create_two_rand_index(array):
        """
        Generate two random indices in the range [0, len(array)).

        Args:
        - array (list): A list for which two random indices need to be generated.

        Returns:
        - tuple: A tuple of two integers representing two random indices in the range [0, len(array)).
        """
        return randint(0, len(array)), randint(0, len(array))

    @staticmethod
    def show_plot(x, y, y_min, y_max, x_label, y_label, title):
        plt.fill_between(x, y_min, y_max, alpha=0.3)
        plt.plot(x, y)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        plt.show()

    @staticmethod
    def write_dict_to_json(dictionary):
        """
        Write a dictionary to a JSON file with indentation for pretty formatting.

        Args:
            dictionary (dict): The dictionary to be written to JSON.

        Returns:
            None
        """
        current_time_millis = int(round(time.time() * 1000))
        log_file_name = f"../resources/solutions/{current_time_millis}.json"

        # Create parent directories if they do not exist
        os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

        with open(log_file_name, 'w') as file:
            json.dump(dictionary, file, indent=4)
