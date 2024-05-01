import pandas as pd
from util.constants import Constants
from base.basemodel import BloodPressureModelTrainer
from util.helpers import create_file_path


PROCESSED_DATA_PATH = Constants.PROCESSOR_FILE_PATH


class TrainBloodPressureModels:
    """
    A class for training blood pressure prediction models.

    Attributes:
    -----------
    data : pd.DataFrame
        The dataset to be used for training the models.

    filepath : str
        The path where model results will be saved.

    bpt : BloodPressureModelTrainer
        A BloodPressureModelTrainer object used for training the models.

    Methods:
    --------
    train_global_models()
        Trains global models and saves the results to an excel file.

    train_region_models()
        Trains regional models and saves the results to an excel file.

    train_country_models()
        Trains country models and saves the results to an excel file.

    train_models()
        Trains all the models (global, regional, and country).

    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the TrainBloodPressureModels class.

        Parameters:
        -----------
        data : pd.DataFrame
            The dataset to be used for training the models.

        """
        self.data = data
        self.bpt = BloodPressureModelTrainer(self.data)

    def train_global_models(self):
        """
        Trains global models and saves the results to an excel file.

        Returns:
        --------
        None
        """
        self.bpt.train_global_models()

    def train_region_models(self):
        """
        Trains regional models and saves the results to an excel file.

        Returns:
        --------
        None
        """
        regions = Constants.REGIONS
        self.bpt.train_regional_models(regions)

    def train_country_models(self):
        """
        Trains country models and saves the results to an excel file.

        Returns:
        --------
        None
        """
        self.bpt.train_country_models()

    def train_models(self):
        """
        Trains all the models (global, regional, and country).

        Returns:
        --------
        None
        """
        self.train_global_models()
        self.train_region_models()
        self.train_country_models()


if __name__ == '__main__':
    data = pd.read_csv(PROCESSED_DATA_PATH, low_memory=False)
    t = TrainBloodPressureModels(data)
    t.train_models()
