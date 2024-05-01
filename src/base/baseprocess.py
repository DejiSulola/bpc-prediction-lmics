import warnings
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from util.constants import Constants

warnings.filterwarnings("ignore")


class DataProcessor:
    def __init__(self, data, categorical_encodings):
        """
        Class constructor.

        Parameters:
        - data: pd.DataFrame
            The input DataFrame to be processed.
        - categorical_encodings: dict
            A dictionary containing the categorical encodings to be used for each categorical variable.
            The keys should be the column names of the categorical variables, and the values should be
            dictionaries that map each category to a numerical encoding.
        """
        self.data = data.copy()
        self.categorical_encodings = categorical_encodings

    def process_numeric_variables(self, data, numeric_cols=None, z_thresh=3):
        """
        Process the numeric variables in the input DataFrame using the Z-score method to remove outliers.

        Parameters:
        - numeric_cols: list of str or None (default: None)
            A list of column names to process. If None, all numeric columns will be processed.
        - z_thresh: float (default: 3)
            The threshold for identifying outliers. Observations with a Z-score greater than z_thresh will be considered
            outliers and removed from the data.

        Returns:
        - pd.DataFrame: The processed DataFrame.
        """
        if numeric_cols is None:
            numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()

        for col in numeric_cols:
            z_scores = (data[col] - data[col].mean()) / data[col].std()
            data = data[(z_scores.abs() < z_thresh) | (data[col].isna())]

        return data


    def process_categorical_variables(self, data, categorical_vars=None, na_value='missing'):
        """
        Process all the categorical variables in the input DataFrame.

        Parameters:
        - categorical_vars: list of str, default=None
            A list of categorical variables to be processed. If not provided, all categorical variables in the DataFrame
            will be processed.
        - na_value: str, default='no response'
            The category value to use for rows without any categorical encoding mapping.

        Returns:
        - pd.DataFrame: The processed DataFrame.
        """
        if categorical_vars is None:
            categorical_cols = data.select_dtypes(include=[object]).columns.tolist()
        else:
            categorical_cols = [col for col in categorical_vars if col in data.columns]

        for col in categorical_cols:
            if col in self.categorical_encodings:
                data[col] = data[col].map(self.categorical_encodings[col])
            else:
                raise Exception(f"Column {col} not found in categorical encodings")

        # Fill missing values in the categorical columns with the na_value
        data[categorical_cols] = data[categorical_cols].apply(lambda x: x.fillna(na_value))

        return data

    def preproc_cols_and_create_targets(self, data):
        """
        Creates a new column in the dataset to classify the blood pressure status of each person.

        Returns:
            None
        """
        # create systolic and diastolic variables
        data[Constants.SYSTOLIC] = data[[Constants.READING1_SYSTOLIC,
                                                   Constants.READING2_SYSTOLIC,
                                                   Constants.READING3_SYSTOLIC]].mean(axis=1)
        data[Constants.DIASTOLIC] = data[[Constants.READING1_DIASTOLIC,
                                                    Constants.READING2_DIASTOLIC,
                                                    Constants.READING3_DIASTOLIC]].mean(axis=1)

        # unify bpm readings
        data[Constants.READING_BPM] = data[[Constants.READING1_BPM,
                                                      Constants.READING2_BPM,
                                                      Constants.READING3_BPM]].mean(axis=1)

        # drop the multiple readings for bpm and systolic, diastolic
        data.drop(Constants.COLUMNS_TO_DROP, axis=1, inplace=True)

        # remove missing values in {systolic, diastolic} feature columns
        data.dropna(subset=[Constants.SYSTOLIC, Constants.DIASTOLIC], inplace=True)

        # Round the systolic and diastolic values
        systolic_rounded = data[Constants.SYSTOLIC].round()
        diastolic_rounded = data[Constants.DIASTOLIC].round()

        # Create a list of blood pressure status based on the rounded values
        blood_pressure = [
            'normal' if systolic < 120 and diastolic < 80 else
            'normal' if 120 <= systolic <= 129 and diastolic < 80 else
            'high' if 130 <= systolic <= 139 or 80 <= diastolic <= 89 else
            'high' if systolic >= 140 or diastolic >= 90 else
            'high' if systolic >= 180 or diastolic >= 120 else
            'high' for systolic, diastolic in zip(systolic_rounded, diastolic_rounded)
        ]
        
        # remove {systolic, diastolic} feature columns
        data.drop([Constants.SYSTOLIC, Constants.DIASTOLIC], axis=1, inplace=True)

        # Add the blood pressure status to the data DataFrame
        data[Constants.TARGET_VARIABLE] = blood_pressure

        return data

    def add_zero_to_missing_values(self):
        """
        Replaces missing values in the DataFrame with 0.

        Returns:
            pandas.DataFrame: A new DataFrame with missing values replaced by 0.
        """
        # replace missing values with 0
        self.data.fillna(value=0, inplace=True)
        return self.data

    def remove_columns_with_missing_values(self, data, missing_threshold=0.8):
        """
        Remove columns from a dataframe that have more than a specified percentage of missing values.

        Parameters:
        missing_threshold (float, optional): The threshold for missing values as a percentage. Default is 0.8 (80%).

        Returns:
        pandas.DataFrame: The input dataframe with columns that have more than missing_threshold percentage of missing values removed.
        """
        # Calculate the percentage of missing values for each column
        missing_percentages = data.isna().sum() / len(data)

        # Find the columns that have a missing percentage greater than the threshold
        columns_to_remove = missing_percentages[missing_percentages > missing_threshold].index

        # Remove the columns from the dataframe
        data = data.drop(columns=columns_to_remove)

        return data

    def create_gold_standard_dataset(self):
        """
        Randomly select 20 percent of records from each country and save it to a csv file as one dataframe representing the gold standard testcase.

        Returns:
            pandas.DataFrame: A new DataFrame with 20 percent records from each country.
        """
        # Group the data by country
        grouped_data = self.data.groupby(Constants.COUNTRY)

        # Create empty dataframes to hold the selected and remaining records
        selected_data = pd.DataFrame(columns=self.data.columns)
        remaining_data = pd.DataFrame(columns=self.data.columns)

        # Loop through each group and randomly select 20% of the records
        for _, group in grouped_data:
            num_records = len(group)
            num_selected = int(num_records * 0.2)
            if num_selected > 0:
                selected_group = group.sample(n=num_selected)
                remaining_group = group.drop(selected_group.index)
            else:
                selected_group = group
                remaining_group = pd.DataFrame(columns=self.data.columns)

            selected_data = selected_data.append(selected_group)
            remaining_data = remaining_data.append(remaining_group)

        # Save the selected data to a CSV file
        selected_data.to_csv(Constants.GOLD_STANDARD_FILE, index=False)
        print(f"Gold standard test data saved to {Constants.GOLD_STANDARD_FILE}")

        return selected_data, remaining_data
    
    def remove_outliers_upper_whisker(self, data, columns):
        df = data[columns]
        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)
        iqr = q3 - q1
        upper_whisker = q3 + Constants.UPPER_MULTIPLIER * iqr

        for col in df.columns:
            mask = df[col] > upper_whisker[col]
            df.loc[mask, col] = np.nan

        data[columns] = df[columns]
        return data

    def remove_outliers_lower_whisker(self, data, columns):
        df = data[columns]
        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - Constants.LOWER_MULTIPLIER * iqr

        for col in df.columns:
            mask = df[col] < lower_bound[col]
            df.loc[mask, col] = np.nan

        data[columns] = df[columns]
        return data

    def handle_missing_values_with_knn(self):
        """Handle missing values using KNN imputer."""

        # Separate the data into numeric and non-numeric subsets
        numeric_data = self.data.select_dtypes(include=[np.number])
        non_numeric_data = self.data.select_dtypes(exclude=[np.number])

        # Apply KNN imputer to the numeric subset
        imputer = KNNImputer(n_neighbors=5)
        imputed_numeric_data = imputer.fit_transform(numeric_data)
        imputed_numeric_df = pd.DataFrame(imputed_numeric_data, columns=numeric_data.columns)

        # Merge the imputed numeric and non-numeric subsets
        self.data = pd.concat([imputed_numeric_df, non_numeric_data], axis=1)

        return self.data




#     def remove_outliers_upper_whisker(self, data, columns, usemean=False):
#         """Replace all values above the upper whisker with a random number between Q1 and Q3.

#         Parameters:
#         data (pandas.DataFrame): The input DataFrame.
#         columns (list): A list of column names to process.

#         Returns:
#         pandas.DataFrame: A modified DataFrame with outliers removed/replaced as appropriate.
#         """
#         # Select only numeric columns
#         # numeric_cols = self.data.select_dtypes(include=['float', 'int']).columns
#         df = data[columns]

#         # Find the quartiles and interquartile range for each column
#         q1 = df.quantile(0.25)
#         q3 = df.quantile(0.75)
#         iqr = q3 - q1

#         # Find the upper whisker for each column
#         upper_whisker = q3 + Constants.UPPER_MULTIPLIER * iqr

#         if usemean:
#             # Replace outliers with random values between the mean and Q3
#             for col in df.columns:
#                 mask = df[col] > upper_whisker[col]
#                 num_outliers = mask.sum()
#                 if num_outliers > 0:
#                     new_values = np.random.uniform(df[col].mean(), q3[col], size=num_outliers)
#                     df.loc[mask, col] = new_values
#         else:
#             # Replace outliers with random values between Q1 and Q3
#             for col in df.columns:
#                 mask = df[col] > upper_whisker[col]
#                 num_outliers = mask.sum()
#                 if num_outliers > 0:
#                     new_values = np.random.uniform(q1[col], q3[col], size=num_outliers)
#                     df.loc[mask, col] = new_values

#         # replace columns in data
#         data[columns] = df[columns]

#         return data

#     def remove_outliers_lower_whisker(self, data, columns, usemean=False):
#         """Replace all values below Q1 with a random number between Q1 and Q3.

#         Parameters:
#         data (pandas.DataFrame): The input DataFrame.
#         columns (list): A list of column names to process.

#         Returns:
#         pandas.DataFrame: A modified DataFrame with outliers removed/replaced as appropriate.
#         """
#         # Select only numeric columns
#         # numeric_cols = df.select_dtypes(include=['float', 'int']).columns
#         df = data[columns]

#         # Find the quartiles and interquartile range for each column
#         q1 = df.quantile(0.25)
#         q3 = df.quantile(0.75)
#         iqr = q3 - q1

#         # Calculate the lower and upper bounds for each column
#         lower_bound = q1 - Constants.LOWER_MULTIPLIER * iqr

#         if usemean:
#             # Replace outliers with random values between Q1 and the mean
#             for col in df.columns:
#                 mask = df[col] < lower_bound[col] # Select values below Q1 instead of above Q3
#                 num_outliers = mask.sum()
#                 if num_outliers > 0:
#                     new_values = np.random.uniform(q1[col], df[col].mean(), size=num_outliers)
#                     df.loc[mask, col] = new_values
#         else:
#             # Replace outliers with random values between Q1 and Q3
#             for col in df.columns:
#                 mask = df[col] < lower_bound[col] # Select values below Q1 instead of above Q3
#                 num_outliers = mask.sum()
#                 if num_outliers > 0:
#                     new_values = np.random.uniform(q1[col], q3[col], size=num_outliers)
#                     df.loc[mask, col] = new_values

#         # replace columns in data
#         data[columns] = df[columns]

#         return data
