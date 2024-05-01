import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from util.constants import Constants
from util.helpers import create_file_path

ANALYZER_PATH = Constants.ANALYZER_PATH

class Analysis:

    def __init__(self, data):
        self.data = data.copy()

    def drop_missing(self, cols):
        """
        Drop rows with missing values for the specified columns.

        Parameters:
        - cols: list of str
            The columns to drop missing values for.
        """
        return self.data.dropna(subset=cols)

    def get_num_rows_before_and_after_drop_missing(self, cols):
        """
        Get the number of rows in the dataset before and after dropping missing values for the specified columns.

        Parameters:
        - cols: list of str
            The columns to drop missing values for.

        Returns:
        - tuple of int
            The number of rows in the dataset before and after dropping missing values.
        """
        num_rows_before = len(self.data)
        missing_df = self.drop_missing(cols)
        num_rows_after = len(missing_df)
        missing_df.reset_index(drop=True, inplace=True)
        result = {
            "Number of rows before dropping missing values": num_rows_before,
            "Number of rows after dropping missing values": num_rows_after
        }
        pprint.pprint(result)

    def get_data_size(self):
        """
        Get the size of the input dataset.

        Returns:
        - dict
            A dictionary containing the number of rows and columns in the dataset.
        """
        rows, cols = self.data.shape
        result = {
            "Number of rows": rows,
            "Number of columns": cols
        }
        pprint.pprint(result)

    def get_unique_values(self, column_name):
        """
        Returns unique values in a given column of a Pandas DataFrame.
        """
        print(f'{self.data[column_name].unique()}')

    def get_missing_values_percentage(self):
        """
        Calculate the percentage of missing values for each column in a dataset.

        Parameters:
        data (pandas.DataFrame): the dataset to analyze

        Returns:
        A pandas.Series with the percentage of missing values for each column in the dataset
        """
        # Get the number of missing values for each column
        missing_values_count = self.data.isnull().sum()

        # Calculate the percentage of missing values for each column
        total_values = self.data.shape[0]
        missing_values_percentage = (missing_values_count / total_values) * 100

        # Return the result as a pandas.Series
        pprint.pprint(missing_values_percentage)

        # Save the pandas Series as an Excel table
        create_file_path(ANALYZER_PATH)
        analyzer_path = f'{ANALYZER_PATH}/mssing_values_column.xlsx'
        missing_values_percentage.to_excel(analyzer_path)
        print(f'Saved report on missing values for each column to excel document: {analyzer_path}')

    def get_country_sample_sizes(self):
        """
        Summarizes the data in a pandas data frame by country and WHO region.

        Parameters:
        df (pandas.DataFrame): A data frame containing observations for multiple countries.

        Returns:
        dict: A dictionary containing the following statistics:
            - 'observations': A data frame containing the total number of observations for each country, paired with the country name and WHO region.
            - 'lowest_obs': A string containing the name of the country with the lowest observation.
            - 'highest_obs': A string containing the name of the country with the highest observation.
            - 'average_size': A float containing the average sample size across the countries.
        """
        # group by country and WHO region, then count the observations
        grouped = self.data.groupby(['country']).size().reset_index(name='Count')

        # get the country with the lowest and highest observation
        lowest_obs = grouped.loc[grouped['Count'].idxmin()]['country']
        highest_obs = grouped.loc[grouped['Count'].idxmax()]['country']

        # get the average sample size
        average_size = grouped['Count'].mean()

        # return the results as a dictionary
        results = {'observations': grouped, 'lowest_obs': lowest_obs, 'highest_obs': highest_obs, 'average_size': average_size}
        pprint.pprint(results)

    def plot_data_sample_size_country_region(self, region_dict):
        """
        Plots the number of observations by country and WHO region in a horizontal bar plot using seaborn.

        Parameters:
        region_dict (dict): A dictionary mapping each country to its corresponding WHO region.

        Returns:
        None
        """
        # Load the data
        df = self.data.copy()

        # Create a dictionary mapping each country to its corresponding WHO region
        country_to_region = {}
        for region, countries in region_dict.items():
            for country in countries:
                country_to_region[country] = region

        # map the countries to their corresponding WHO region
        df['WHO Region'] = df['country'].map(country_to_region)

        # group by country and WHO region, then count the observations
        grouped = df.groupby(['country', 'WHO Region']).size().reset_index(name='Count')

        # remove regions with no observations
        grouped = grouped.dropna()

        # set the seaborn style
        sns.set(style="whitegrid")

        # set the seaborn style and figure size
        # sns.set(style="whitegrid", rc={"figure.figsize":(12,6)})
        sns.set(style="whitegrid", rc={"figure.figsize":(11.7, 8.27)}) # A4 landscape size

        # set the bar width
        bar_width = 0.8

        # create the bar plot
        if not grouped.empty:
            # sort the bars by WHO region
            regions = list(region_dict.keys())
            # regions = [region.replace('_', ' ') for region in regions]
            regions.sort()

            # capitalize the first letter of each country name
            grouped['country'] = grouped['country'].apply(lambda x: x.capitalize())
            # replace underscores with spaces in WHO region names
            grouped['WHO Region'] = grouped['WHO Region'].replace('_', ' ')

            ax = sns.barplot(x="country", y="Count", hue="WHO Region", data=grouped, palette="deep", saturation=.8, order=grouped.sort_values('WHO Region').country.unique(), hue_order=regions)

            # ax = sns.barplot(x="country", y="Count", hue="WHO Region", data=grouped, palette="deep", saturation=.8)

            # set the title and axes labels
            plt.title('Number of observations by country and WHO region')
            plt.xlabel('Country')
            plt.ylabel('Count')

            # rotate and slant the country labels
            ax.set_xticklabels(ax.get_xticklabels(), rotation=-90, ha='left')

            # replace underscores with spaces in the legend display
            handles, labels = ax.get_legend_handles_labels()
            labels = [label.replace('_', ' ') for label in labels]
            ax.legend(handles=handles, labels=labels)

            # set the width of the bars
            for patch in ax.patches:
                current_width = patch.get_width()
                diff = current_width - bar_width
                patch.set_width(bar_width)
                patch.set_x(patch.get_x() + diff * 0.5)

            # show the plot
            # plt.show()
            plt.savefig(f'../paper/image/plot_data_sample_size_country_region.png', dpi=800, bbox_inches='tight')
            
            # save the plot as a PDF
            plt.savefig(f'../paper/image/plot_data_sample_size_country_region.pdf', format='pdf', dpi=800, bbox_inches='tight', orientation='landscape')
        else:
            print("No data to plot.")
