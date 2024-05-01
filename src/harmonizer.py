import os
import glob
import pandas as pd

from util.constants import Constants
from util.helpers import draw_multiple_box_plot
from util.helpers import create_file_path

FOLDER_PATH = 'data/cleaned'
OUTPUT_FILE_PATH = Constants.HARMONIZER_FILE_PATH
PLOT_OUTPUT = Constants.PLOT_PATH+'/harmonized'
FILENAME = 'harmonized.png'

class CsvHarmonizer:
    """
    A class to combine multiple CSV files into one.

    Args:
    folder_path (str): The folder path containing the CSV files to be combined.
    output_file_path (str): The output file path to save the combined CSV file.
    """

    def __init__(self, folder_path, output_file_path):
        self.folder_path = folder_path
        self.output_file_path = output_file_path

    def validate_csvs(self, csv_files):
        """
        Validate that the CSV files have the same number of columns.

        Args:
        csv_files (list): A list of CSV file paths to validate.

        Returns:
        bool: True if all CSV files have the same number of columns, otherwise False.
        """
        column_count = None
        for csv_file in csv_files:
            df = pd.read_csv(csv_file, low_memory=False)
            if column_count is None:
                column_count = len(df.columns)
            elif len(df.columns) != column_count:
                return False
        return True

    def combine_csvs(self):
        """
        Combine multiple CSV files into one.

        Returns:
        None
        """
        csv_files = glob.glob(os.path.join(self.folder_path, "*.csv"))
        if not csv_files:
            print(f"No CSV files found in {self.folder_path}")
            return

        if not self.validate_csvs(csv_files):
            print("CSV files do not have the same number of columns")
            return

        combined_csv = pd.concat([pd.read_csv(f, low_memory=False) for f in csv_files], ignore_index=True)

        create_file_path(self.output_file_path)

        combined_csv.to_csv(self.output_file_path, index=False)
        print(f"Combined CSV file saved to {self.output_file_path}")

    def run(self):
        """
        Execute the CSV combining process.

        Returns:
        None
        """
        self.combine_csvs()

        # draw box plot of numeric variables
        draw_multiple_box_plot(data_path=OUTPUT_FILE_PATH, variables=Constants.NUMERIC_VARIABLES_PLOT,
                               save_location=PLOT_OUTPUT, filename=FILENAME)

        if not os.path.exists(os.path.dirname(PLOT_OUTPUT)):
            os.makedirs(os.path.dirname(PLOT_OUTPUT))

        print(f"Saved numeric boxplots to {PLOT_OUTPUT}")

if __name__ == "__main__":
    combiner = CsvHarmonizer(FOLDER_PATH, OUTPUT_FILE_PATH)
    combiner.run()
