import warnings
import pandas as pd
from util.constants import Constants
from util.helpers import create_file_path
from sklearn.model_selection import train_test_split

# suppress FutureWarning and DataConversionWarning messages
warnings.filterwarnings("ignore", category=FutureWarning)

def numeric_summary(dataset):
    # Select only numeric columns
    numeric_cols = dataset.select_dtypes(include=['float', 'int']).columns
    dataset = dataset[numeric_cols]

    # Perform train-test split with 80% train data and 20% test data
    train_data, test_data = train_test_split(dataset, test_size=0.2)

    # Calculate mean and standard deviation for each column in the total dataset
    total_mean = dataset.mean()
    total_std = dataset.std()

    # Calculate mean and standard deviation for each column in the train dataset
    train_mean = train_data.mean()
    train_std = train_data.std()

    # Calculate mean and standard deviation for each column in the test dataset
    test_mean = test_data.mean()
    test_std = test_data.std()

    # Create a dataframe with the results
    result_df = pd.DataFrame({'Column Name': dataset.columns,
                              'Total Mean': total_mean,
                              'Total Std': total_std,
                              'Train Mean': train_mean,
                              'Train Std': train_std,
                              'Test Mean': test_mean,
                              'Test Std': test_std})

    # Save the results to an Excel file
    filepath = 'results/baseline_characteristics'
    create_file_path(filepath)
    result_df.to_excel(f'{filepath}/numeric_table.xlsx', index=False)


def categorical_summary(df):
    """
    Creates a table providing the baseline characteristics of categorical variables in a dataset.

    Parameters:
    -----------
    df : pandas DataFrame
        The dataset containing the categorical variables to be analyzed.

    Returns:
    --------
    None
    """

    # Split data into training and test sets
    train_df, test_df = train_test_split(df, test_size=0.2,)

    # Create a list of categorical columns
    cat_cols = df.select_dtypes(include=['category', 'object']).columns.tolist()

    # remove 'Country' variables
    cat_cols.remove('country')

    # Create an empty DataFrame to store the summary statistics
    summary = pd.DataFrame()

    # Loop through each categorical variable and create summary statistics
    for var_name in cat_cols:

        var_summary = pd.DataFrame()

        total_pop = df[var_name].value_counts()
        total_percent = (total_pop / total_pop.sum()) * 100

        train_pop = train_df[var_name].value_counts()
        train_percent = (train_pop / train_pop.sum()) * 100

        test_pop = test_df[var_name].value_counts()
        test_percent = (test_pop / test_pop.sum()) * 100

        # Concatenate Series
        var_summary[f'Total population n={len(df)}'] = pd.concat([total_pop, total_percent], axis=1)\
                                         .apply(lambda x: f'{x[0]} ({x[1]:.2f})', axis=1)
        var_summary[f'Train dataset n={len(train_df)}'] = pd.concat([train_pop, train_percent], axis=1)\
                                        .apply(lambda x: f'{x[0]} ({x[1]:.2f})', axis=1)
        var_summary[f'Test dataset n={len(test_df)}'] = pd.concat([test_pop, test_percent], axis=1)\
                                        .apply(lambda x: f'{x[0]} ({x[1]:.2f})', axis=1)

        var_summary.reset_index(drop=False, inplace=True)  # convert index to column
        var_summary.rename(columns={'index': 'Category'}, inplace=True)

        var_summary['Variable'] = var_name

        # Append to the summary DataFrame
        summary = summary.append(var_summary)

    # Save table as Excel file
    filepath = 'results/baseline_characteristics'
    create_file_path(filepath)
    writer = pd.ExcelWriter(f'{filepath}/categorical_summary.xlsx')
    summary.to_excel(writer, index=False)
    writer.save()


my_dataset = pd.read_csv(Constants.BASELINE_FILE_PATH, low_memory=False)
numeric_summary(my_dataset)
categorical_summary(my_dataset)