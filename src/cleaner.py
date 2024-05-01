import glob
import pandas as pd
from util.constants import Constants
from util.helpers import get_class_names

from clean.kiribati import Kiribati
from clean.grenada import Grenada
from clean.libya import Libya
from clean.lao_people_democratic_republic import LaoPeopleDemocraticRepublic
from clean.comoros import Comoros
from clean.cote_divoire import CoteDivoire
from clean.chad import Chad
from clean.algeria import Algeria
from clean.uganda import Uganda
from clean.barbados import Barbados
from clean.french_polynesia import FrenchPolynesia
from clean.mali import Mali
from clean.american_samoa import AmericanSamoa
from clean.palau import Palau
from clean.guinea import Guinea
from clean.namibia import Namibia
from clean.tuvalu import Tuvalu
from clean.democratic_republic_of_the_congo import DemocraticRepublicOfTheCongo
from clean.niger import Niger
from clean.vanuatu import Vanuatu
from clean.fiji import Fiji
from clean.timor_leste import TimorLeste
from clean.bahamas import Bahamas
from clean.cayman_islands import CaymanIslands
from clean.tokelau import Tokelau
from clean.mauritania import Mauritania
from clean.solomon_islands import SolomonIslands
from clean.myanmar import Myanmar
from clean.cook_islands import CookIslands
from clean.qatar import Qatar
from clean.sierra_leone import SierraLeone
from clean.nauru import Nauru
from clean.british_virgin_islands import BritishVirginIslands
from clean.ghana import Ghana
from clean.gabon import Gabon
from clean.liberia import Liberia
from clean.malawi import Malawi
from clean.eswatini import Eswatini
from clean.micronesia import Micronesia
from clean.kyrgyzstan import Kyrgyzstan
from clean.benin import Benin
from clean.palestine import Palestine
from clean.ethiopia import Ethiopia
from clean.armenia import Armenia
from clean.guyana import Guyana
from clean.mongolia import Mongolia
from clean.ecuador import Ecuador
from clean.azerbaijan import Azerbaijan
from clean.sri_lanka import SriLanka
from clean.eritrea import Eritrea
from clean.lesotho import Lesotho
from clean.niue import Niue
from clean.afghanistan import Afghanistan
from clean.madagascar import Madagascar
from clean.belarus import Belarus
from clean.gambia import Gambia
from clean.togo import Togo
from clean.bangladesh import Bangladesh
from clean.botswana import Botswana
from clean.bhutan import Bhutan
from clean.mozambique import Mozambique
from clean.maldives import Maldives
from clean.central_african_republic import CentralAfricanRepublic
from clean.georgia import Georgia
from clean.samoa import Samoa
from clean.tanzania import Tanzania
from clean.zambia import Zambia
from clean.rwanda import Rwanda
from clean.moldova import Moldova
from clean.nepal import Nepal
from clean.tonga import Tonga

class DataCleaner:
    """
    A class for cleaning a CSV dataset.

    Attributes:
    files (list of str): List of paths to the input CSV files.
    cleaned_data (pandas.DataFrame): Data stored in a pandas DataFrame after cleaning.
    """

    def __init__(self):
        """
        Initialize the DataCleaner class with the list of file paths.

        Args:
        files (list of str): List of paths to the input CSV files.
        """
        self.files = None
        self.cleaned_data = pd.DataFrame()

    def _load_data(self):
        """
        Load the CSV data into a list of file paths.

        Loads the list of paths to the various country datasets using glob.glob().
        """
        path = Constants.RAW_DATA_FILE_PATH
        self.files = glob.glob(path, recursive=True)

    def _clean_data(self):
        """
        Clean the data in each CSV file.

        Reads the CSV files and runs the cleaning job for each country by executing the matching class.
        """
        class_names = get_class_names("clean/")

        for file in self.files:
            country_name = file.split('/')[2]

            if country_name in [class_name.lower() for class_name in class_names]:
                # Get the index of the matching class name
                index = [class_name.lower() for class_name in class_names].index(country_name)
                # Get the class name from the original class_names list
                class_to_execute = class_names[index]
                # Read the dataframe from the file loop
                df = pd.read_csv(file, low_memory=False, encoding='latin-1')
                # Execute the class
                print(f'class: {class_to_execute}')
                exec(f'{class_to_execute}(df).run_cleaning()')

    def run(self):
        """
        Run the cleaning process for the CSV datasets.
        """
        self._load_data()
        self._clean_data()

if __name__ == "__main__":
    DataCleaner().run()
