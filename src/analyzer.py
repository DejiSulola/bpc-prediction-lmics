import pandas as pd

from util.constants import Constants
from base.baseanalysis import Analysis

PROCESSED_FILE = Constants.PROCESSOR_FILE_PATH
HARMONIZED_FILE = Constants.HARMONIZER_FILE_PATH

class AnalysisExecutor:
    def __init__(self, data):
        self.analysis = Analysis(data)

    def execute(self):
        cols_to_drop_missing = [Constants.SYSTOLIC, Constants.DIASTOLIC]
        # self.analysis.get_num_rows_before_and_after_drop_missing(cols_to_drop_missing)
        self.analysis.get_data_size()
        self.analysis.get_unique_values(Constants.TARGET_VARIABLE)
        self.analysis.get_missing_values_percentage()
        self.analysis.get_country_sample_sizes()
        self.analysis.plot_data_sample_size_country_region(Constants.REGIONS)

if __name__ == "__main__":
    # Load data
    data = pd.read_csv(PROCESSED_FILE, low_memory=False)
    # Create executor
    executor = AnalysisExecutor(data)
    # Execute analysis
    executor.execute()
