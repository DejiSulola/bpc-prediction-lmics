import os
import pandas as pd
import numpy as np
from base.baseprocess import DataProcessor
from util.constants import Constants
from util.mapping import CategoricalMapping
from util.helpers import draw_multiple_box_plot
from util.helpers import create_file_path

INPUT_FILE = Constants.HARMONIZER_FILE_PATH
OUTPUT_FILE = Constants.PROCESSOR_FILE_PATH

PLOT_OUTPUT = Constants.PLOT_PATH+'/processed'
FILENAME = 'processed.png'

class Processor:
    """
    A class for processing CSV files using the DataProcessor class and saving the result to a new file.

    Args:
    - input_file_path (str): The path to the input CSV file.
    - output_file_path (str): The path to the output CSV file.
    - cat_mapping (dict): A dictionary containing a mapping for the categorical encoding.

    Methods:
    - process_csv: Processes the input CSV file and saves the result to the output CSV file.
    """

    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def process_csv(self):
        """
        Processes the input CSV file and saves the result to the output CSV file.
        """
        if not os.path.exists(self.input_file_path):
            raise FileNotFoundError(f"Input file {self.input_file_path} not found.")

        # import data
        data = pd.read_csv(self.input_file_path, low_memory=False)

        # Create the DataProcessor instance and process the data
        processor = DataProcessor(data, CategoricalMapping.get_mappings())

        # create gold standard test file
        # _, processed_data = processor.create_gold_standard_dataset()

        # process numeric variables
        processed_data = processor.process_numeric_variables(processed_data, Constants.PROCESSOR_NUMERIC_COLS)
        # process categorical variables
        processed_data = processor.process_categorical_variables(processed_data, Constants.PROCESSOR_CATEGORICAL_COLS)
        # preprocess columns and create targets
        processed_data = processor.preproc_cols_and_create_targets(processed_data)
        # remove column with more than 80% missing value
        processed_data = processor.remove_columns_with_missing_values(processed_data)
        # prune numeric variables with nonsensical outliers
        processed_data = processor.remove_outliers_upper_whisker(processed_data, columns=Constants.OUTLIER_UPPER_WHISKER)
        processed_data = processor.remove_outliers_lower_whisker(processed_data, columns=Constants.OUTLIER_LOWER_WHISKER)
        processed_data = processor.remove_outliers_upper_whisker(processed_data, columns=Constants.CHOLESTEROL_VARS)
        processed_data = processor.remove_outliers_lower_whisker(processed_data, columns=Constants.CHOLESTEROL_VARS)
        # processed_data = processor.handle_missing_values_with_knn()
        
        # draw box plot of numeric variables - select numeric columns using select_dtypes()
        create_file_path(PLOT_OUTPUT)
        numeric_cols = processed_data.select_dtypes(include=np.number).columns.tolist()
        draw_multiple_box_plot(data=processed_data, variables=numeric_cols,
                               save_location=PLOT_OUTPUT, filename=FILENAME)
        print(f"Saved numeric boxplots to {PLOT_OUTPUT}")

        # Save the processed data for baseline characterstic calculation to the output file
        processed_data.to_csv(Constants.BASELINE_FILE_PATH, index=False)
        print(f"Baseline data saved to {Constants.BASELINE_FILE_PATH}")


        # fill missing values with 0
        # processor.add_zero_to_missing_values()

        # Save the processed data to the output file
        processed_data.to_csv(self.output_file_path, index=False)
        print(f"Processed data saved to {self.output_file_path}")


if __name__ == "__main__":
    # Process the CSV and save the result to the output file
    csv_processor = Processor(INPUT_FILE, OUTPUT_FILE)
    csv_processor.process_csv()
