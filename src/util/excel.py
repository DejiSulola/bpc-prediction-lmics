import os
import pandas as pd

def recast_excel_file(input_path, output_path):
    """
    Reads an Excel file with the headers [model, accuracy, accuracy_std, precision, precision_std, recall, recall_std, f1, f1_std],
    recasts the columns in the excel table to have the following structure:
    model, round(accuracy *100, 2) (round(accuracy_std *100, 2)), round(precision *100, 2) (round(precision_std *100, 2)),
    round(recall *100, 2) (round(recall_std *100, 2)), round(f1 *100, 2) (round(f1_std *100, 2)) with the headers:
    Model, Accuracy, F1, Precision, Recall and writes the new dataframe to excel.

    :param input_path: The path of the input Excel file.
    :type input_path: str
    :param output_path: The path of the output Excel file.
    :type output_path: str
    :return: None
    """
    # Read the input Excel file
    df = pd.read_excel(input_path)

    # Rename columns
    df = df.rename(columns={
        'model': 'Model',
        'accuracy': 'Accuracy',
        'accuracy_std': 'Accuracy_std',
        'precision': 'Precision',
        'precision_std': 'Precision_std',
        'recall': 'Recall',
        'recall_std': 'Recall_std',
        'f1': 'F1',
        'f1_std': 'F1_std'
    })

    # Recast columns
    df['Accuracy'] = round(df['Accuracy'] * 100, 2).astype(str) + ' (' + round(df['Accuracy_std'] * 100, 2).astype(str) + ')'
    df['F1'] = round(df['F1'] * 100, 2).astype(str) + ' (' + round(df['F1_std'] * 100, 2).astype(str) + ')'
    df['Precision'] = round(df['Precision'] * 100, 2).astype(str) + ' (' + round(df['Precision_std'] * 100, 2).astype(str) + ')'
    df['Recall'] = round(df['Recall'] * 100, 2).astype(str) + ' (' + round(df['Recall_std'] * 100, 2).astype(str) + ')'

    # Select required columns
    df = df[['Model', 'Accuracy', 'F1', 'Precision', 'Recall']]

    # Sort the dataframe
    df = df.sort_values(by=['Model'])

    # Write the new dataframe to Excel
    df.to_excel(output_path, index=False)


def merge_excel_files(folder_path, output_path):
    """
    Reads all Excel files in a folder, merges them into one dataframe and writes the new dataframe to Excel.

    :param folder_path: The path of the folder containing the Excel files.
    :type folder_path: str
    :param output_path: The path of the output Excel file.
    :type output_path: str
    :return: None
    """
    # Get a list of all Excel files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    # Read all Excel files and merge them into one dataframe
    df = pd.concat([pd.read_excel(os.path.join(folder_path, f)) for f in files], ignore_index=True)

    # Write the new dataframe to Excel
    df.to_excel(output_path, index=False)

import os
import pandas as pd

def recast_and_merge_excel_files(folder_path, output_path, is_country=False):
    """
    Reads all Excel files in a folder, recasts the columns in the excel table to have the following structure:
    region, model, round(accuracy *100, 2) (round(accuracy_std *100, 2)), round(precision *100, 2) (round(precision_std *100, 2)),
    round(recall *100, 2) (round(recall_std *100, 2)), round(f1 *100, 2) (round(f1_std *100, 2)), shape with the headers:
    Region or Country, Model, Accuracy, F1, Precision, Recall, Shape, merges them into one dataframe and writes the new dataframe to Excel.

    :param folder_path: The path of the folder containing the Excel files.
    :type folder_path: str
    :param output_path: The path of the output Excel file.
    :type output_path: str
    :param is_country: True if the Excel files have a 'Country' column instead of a 'Region' column, False otherwise.
    :type is_country: bool
    :return: None
    """
    # Get a list of all Excel files in the folder
    files = sorted([f for f in os.listdir(folder_path) if f.endswith('.xlsx')])

    # Read all Excel files and concatenate them into one dataframe
    dfs = []
    for f in files:
        df = pd.read_excel(os.path.join(folder_path, f))

        # Replace all but the first cell of the 'Country' or 'Region' column with '~'
        if is_country:
            df.loc[1:, 'country'] = '~'
        else:
            df.loc[1:, 'region'] = '~'

        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    # Rename columns
    if is_country:
        df = df.rename(columns={
            'country': 'Country',
            'model': 'Model',
            'accuracy': 'Accuracy',
            'accuracy_std': 'Accuracy_std',
            'precision': 'Precision',
            'precision_std': 'Precision_std',
            'recall': 'Recall',
            'recall_std': 'Recall_std',
            'f1': 'F1',
            'f1_std': 'F1_std',
            'shape': 'Shape'
        })
        df['Country'] = df['Country'].apply(lambda x: x.title())
    else:
        df = df.rename(columns={
            'region': 'Region',
            'model': 'Model',
            'accuracy': 'Accuracy',
            'accuracy_std': 'Accuracy_std',
            'precision': 'Precision',
            'precision_std': 'Precision_std',
            'recall': 'Recall',
            'recall_std': 'Recall_std',
            'f1': 'F1',
            'f1_std': 'F1_std',
            'shape': 'Shape'
        })
        df['Region'] = df['Region'].str.replace('_', ' ')
        df['Region'] = df['Region'].apply(lambda x: x.title())
        df['Region'] = df['Region'].str.replace(' And ', ' \& ')

    # Recast columns
    df['Accuracy'] = round(df['Accuracy'] * 100, 2).astype(str) + ' (' + round(df['Accuracy_std'] * 100, 2).astype(str) + ')'
    df['F1'] = round(df['F1'] * 100, 2).astype(str) + ' (' + round(df['F1_std'] * 100, 2).astype(str) + ')'
    df['Precision'] = round(df['Precision'] * 100, 2).astype(str) + ' (' + round(df['Precision_std'] * 100, 2).astype(str) + ')'
    df['Recall'] = round(df['Recall'] * 100, 2).astype(str) + ' (' + round(df['Recall_std'] * 100, 2).astype(str) + ')'

    # Check if the required columns are present
    if is_country:
        required_columns = ['Country', 'Model', 'Accuracy', 'F1', 'Precision', 'Recall', 'Shape']
    else:
        required_columns = ['Region', 'Model', 'Accuracy', 'F1', 'Precision', 'Recall', 'Shape']
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f'The following columns are missing from the Excel files: {missing_columns}')

    # Select required columns
    df = df[required_columns]

    # Write the new dataframe to Excel
    df.to_excel(output_path, index=False)
