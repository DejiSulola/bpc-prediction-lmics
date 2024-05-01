import os
import re
from util.generator import BoxPlotGenerator

def save_cleaned_data(cleaned_data, file_path, file_name, extension=".csv"):
    """
    Save the cleaned data to a new CSV file.

    Args:
        cleaned_data (pandas DataFrame): The cleaned data to be saved.
        file_path (str): The path to the directory where the output CSV file should be saved.
        file_name (str): The name of the output CSV file, without the extension.
        extension (str, optional): The extension for the output CSV file. Defaults to '.csv'.

    Returns:
        None
    """
    strings = [file_path, str.lower(file_name)+extension]
    separator = "/"

    save_path = separator.join(strings)

    create_file_path(save_path)

    cleaned_data.to_csv(save_path, index=False)


def get_class_names(directory):
    """
    Extract the names of all base classes from Python files in a directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search for Python files.

    Returns:
        list: A list of strings containing the names of all base classes.
    """
    class_names = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                with open(os.path.join(dirpath, filename)) as f:
                    content = f.read()
                    matches = re.findall(r'class\s+(\w+)\b(?!.*\b(?:extends|inherits)\b)', content)
                    for match in matches:
                        class_names.append(match)

    class_names = [name for name in class_names if name != 'with']

    return class_names


def draw_single_box_plot(data, variable, save_location, style=1):
    """
    Draw a box plot of a single variable and save it to a file.

    Args:
        variable (str): The name of the variable to plot.
        data (str): The path to the CSV file containing the data.
        save_location (str): The path to save the resulting plot image.

    Returns:
        None
    """
    # Instantiate BoxPlotGenerator object
    bpg = BoxPlotGenerator(data)

    # Draw box plots for variables
    if style == 1:
        bpg.draw_box_plots_single_1(variable, save_path=save_location)
    else:
        bpg.draw_box_plots_single_2(variable, save_path=save_location)


def draw_multiple_box_plot(variables, save_location, filename = None, title = None, data = None, data_path=None):
    """
    Draw a box plot of a multiple variables and save it to a file.

    Args:
        variables (str): The variable name to plot (in a list).
        data (str): The path to the CSV file containing the data.
        save_location (str): The path to save the resulting plot image.
        title (str): The tile of the resulting plot image.

    Returns:
        None
    """
    # Instantiate BoxPlotGenerator object
    bpg = BoxPlotGenerator(data=data, data_path=data_path)

    # Draw box plots for variables
    bpg.draw_box_plots_multiple(variables,
                                save_path=save_location,
                                filename=filename,
                                title=title)

def create_file_path(file_path):
    """
    Create file path if it does not exist.

    Parameters:
    - file_path: str
        The file path to create.

    Returns:
    - None
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path)