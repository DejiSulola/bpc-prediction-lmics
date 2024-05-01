import os
import pickle
import warnings
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from pprint import pprint
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.inspection import permutation_importance

from util.constants import Constants
from util.helpers import create_file_path

# suppress FutureWarning and DataConversionWarning messages
warnings.filterwarnings("ignore", category=FutureWarning)

MODELLING_FILE_PATH = Constants.MODELLING_FILE_PATH

class BloodPressureModelTrainer:
    """
    A class for training and saving blood pressure prediction models.

    ...

    Attributes
    ----------
    data : pd.DataFrame
        The data to use for training the models.

    Methods
    -------
    _preprocess_data()
        Preprocesses the data by one-hot encoding categorical variables and scaling the data using StandardScaler.

    train_global_models(models)
        Trains global models using the entire dataset.

    train_regional_models(models, regions)
        Trains regional models by region.

    train_country_models(models)
        Trains country models by country.
    """

    def __init__(self, data):
        """
        Initializes a new instance of the BloodPressureModelTrainer class.

        Parameters
        ----------
        data : pd.DataFrame
            The data to use for training the models.
        """
        self.data = data.copy()
        self.models = Constants.MODELS
        self.resultpath = Constants.MODEL_RESULTS

        # Preprocess data
        self._preprocess_data()

    def _preprocess_data(self):
        """
        Preprocesses the data by one-hot encoding categorical variables and scaling numerical variables using StandardScaler.
        """
        create_file_path(MODELLING_FILE_PATH)
        modelling_path = f'{MODELLING_FILE_PATH}/modelling.csv'

        # Save the modelling data to the output file if it doesn't already exist
        if not os.path.isfile(modelling_path):
            # One-hot encode categorical variables
            for col in Constants.MODEL_CATEGORICAL_COLS:
                dummies = pd.get_dummies(self.data[col], prefix=col, drop_first=True)
                self.data = pd.concat([self.data, dummies], axis=1)
                self.data.drop(col, axis=1, inplace=True)

            # Scale the numeric variables using z-scores
            # self.data[Constants.MODEL_NUMERIC_COLS] = scale(self.data[Constants.MODEL_NUMERIC_COLS])
            # Prescale the numeric variables by dividing by their standard deviation
            scaler = StandardScaler()
            self.data[Constants.MODEL_NUMERIC_COLS] = scaler.fit_transform(self.data[Constants.MODEL_NUMERIC_COLS])

            # Save the modelling data to the output file
            self.data.to_csv(modelling_path, index=False)
            print(f"Modelling data saved to {MODELLING_FILE_PATH}")
        else:
            self.data = pd.read_csv(modelling_path)

    def train_global_models(self):
        """
        Trains global models using the entire dataset.

        Parameters
        ----------
        models : dict
            A dictionary of models to train.

        Returns
        -------
        pd.DataFrame
            The metrics for each model.
        """

        create_file_path(f'{self.resultpath}/global/models')

        # Train and evaluate models
        results = []

        for name in self.models.keys():
            clf = self.models[name]

            # check if saved model exists, if yes, skip training
            if os.path.exists(f'{Constants.MODEL_PATH}/global/{name}_global.pkl'):
                print(f'{name}_global.pkl: already exists')
                continue

            print(f'training -> {name}_global')

            # Shuffle the data randomly
            data_shuffled = self.data.sample(frac=1, random_state=42)

            X = data_shuffled.drop([Constants.COUNTRY, Constants.SYSTOLIC, Constants.DIASTOLIC, Constants.TARGET_VARIABLE], axis=1)
            y = data_shuffled[Constants.TARGET_VARIABLE]
            y = LabelEncoder().fit_transform(y.values.ravel())
            scores = cross_validate(clf, X, y, cv=10, scoring=('accuracy', 'precision', 'recall', 'f1'))
            result = {
                'model': name,
                'accuracy': scores['test_accuracy'].mean(),
                'accuracy_std': scores['test_accuracy'].std(),
                'precision': scores['test_precision'].mean(),
                'precision_std': scores['test_precision'].std(),
                'recall': scores['test_recall'].mean(),
                'recall_std': scores['test_recall'].std(),
                'f1': scores['test_f1'].mean(),
                'f1_std': scores['test_f1'].std()
            }
            pprint(result)
            results.append(result)

            # Save model as a pickle file
            filepath = f'{Constants.MODEL_PATH}/global'
            create_file_path(filepath)
            with open(f'{filepath}/{name}_global.pkl', 'wb') as file:
                pickle.dump(clf, file)

            # save results
            pd.DataFrame([result]).to_excel(f'{self.resultpath}/global/models/{name}_global.xlsx', index=False)

        # save results
        if len(results) > 0:
            pd.DataFrame(results).to_excel(f'{self.resultpath}/global/global_models.xlsx', index=False)

        # Evaluate feature importances
        print("Evaluating feature importance")
        self.evaluate_feature_importance('RF')


    def train_regional_models(self, regions):
        """
        Trains a model for each region.

        Parameters:
        - models: dict
            The dictionary of models to train.
        - regions: dict
            A dictionary of regions and the countries they contain.

        Returns:
        - pd.DataFrame
            The metrics for each region.
        """

        for region, countries in regions.items():
            region_data = self.data[self.data[Constants.COUNTRY].isin(countries)]

            # Create folder for saving the results
            create_file_path(f'{self.resultpath}/region/{region}')
            # Create folder for saving the model
            create_file_path(f'{Constants.MODEL_PATH}/region/{region}')

            region_results = []

            for model_name, model in self.models.items():
                # Check if the model has already been trained and saved
                modelpath = f'{Constants.MODEL_PATH}/region/{region}/{region}_{model_name}.pkl'

                # check if saved model exists, if yes, skip training
                if os.path.exists(modelpath):
                    print(f'{region}_{model_name}.pkl: already exists')
                    continue

                print(f'training -> {region}_{model_name}')

                # Shuffle the data randomly
                data_shuffled = region_data.sample(frac=1, random_state=42)

                X = data_shuffled.drop([Constants.COUNTRY, Constants.TARGET_VARIABLE], axis=1)
                y = data_shuffled[Constants.TARGET_VARIABLE]
                y = LabelEncoder().fit_transform(y.values.ravel())
                scores = cross_validate(model, X, y, cv=10, scoring=('accuracy', 'precision', 'recall', 'f1'))

                result = {
                    'region': region,
                    'model': model_name,
                    'shape': data_shuffled.shape,
                    'accuracy': scores['test_accuracy'].mean(),
                    'accuracy_std': scores['test_accuracy'].std(),
                    'precision': scores['test_precision'].mean(),
                    'precision_std': scores['test_precision'].std(),
                    'recall': scores['test_recall'].mean(),
                    'recall_std': scores['test_recall'].std(),
                    'f1': scores['test_f1'].mean(),
                    'f1_std': scores['test_f1'].std()
                }

                pprint(result)
                region_results.append(result)

                # Save model as a pickle file
                with open(modelpath, 'wb') as f:
                    pickle.dump(model, f)

                # save results
                pd.DataFrame([result]).to_excel(f'{self.resultpath}/region/{region}/{region}_{model_name}.xlsx', index=False)

            # save results
            pd.DataFrame(region_results).to_excel(f'{self.resultpath}/region/{region}_models.xlsx', index=False)


    def train_country_models(self):
        """
        Trains a model for each country in the dataset.

        Parameters:
        - models: dict
            The dictionary of models to train.
        - countries: dict
            A dictionary of countries and the countries they contain.

        Returns:
        - pd.DataFrame
            The metrics for each country.
        """

        for country in self.data[Constants.COUNTRY].unique():
            country_data = self.data[self.data[Constants.COUNTRY] == country]

            # Create folder for saving the results
            create_file_path(f'{self.resultpath}/countries/{country}')
            # Create folder for saving the model
            create_file_path(f'{Constants.MODEL_PATH}/countries/{country}')

            country_results = []

            for model_name, model in self.models.items():
                # Check if the model has already been trained and saved
                modelpath = f'{Constants.MODEL_PATH}/countries/{country}/{country}_{model_name}.pkl'

                # check if saved model exists, if yes, skip training
                if os.path.exists(modelpath):
                    print(f'{country}_{model_name}.pkl: already exists')
                    continue

                print(f'training -> {country}_{model_name}')

                # Shuffle the data randomly
                data_shuffled = country_data.sample(frac=1, random_state=42)

                X = data_shuffled.drop([Constants.COUNTRY, Constants.TARGET_VARIABLE], axis=1)
                y = data_shuffled[Constants.TARGET_VARIABLE]
                y = LabelEncoder().fit_transform(y.values.ravel())
                scores = cross_validate(model, X, y, cv=10, scoring=('accuracy', 'precision', 'recall', 'f1'))

                result = {
                    'country': country,
                    'model': model_name,
                    'shape': data_shuffled.shape,
                    'accuracy': scores['test_accuracy'].mean(),
                    'accuracy_std': scores['test_accuracy'].std(),
                    'precision': scores['test_precision'].mean(),
                    'precision_std': scores['test_precision'].std(),
                    'recall': scores['test_recall'].mean(),
                    'recall_std': scores['test_recall'].std(),
                    'f1': scores['test_f1'].mean(),
                    'f1_std': scores['test_f1'].std()
                }

                pprint(result)
                country_results.append(result)

                # Save model as a pickle file
                with open(modelpath, 'wb') as f:
                    pickle.dump(model, f)

                # save results
                pd.DataFrame([result]).to_excel(f'{self.resultpath}/countries/{country}/{country}_{model_name}.xlsx', index=False)

            # save results
            pd.DataFrame(country_results).to_excel(f'{self.resultpath}/countries/{country}_models.xlsx', index=False)


    def evaluate_feature_importance(self, model_name):
        """
        Evaluates the feature importance of a given model using mean decrease in impurity and feature permutation importance.
        Writes the results to an excel file.

        Parameters
        ----------
        model_name : str
            The name of the model to evaluate.

        Returns
        -------
        None
        """

        result_path = f'{self.resultpath}/global/feature_importance'
        create_file_path(result_path)
        excel_file_path = f'{result_path}/{model_name}_global_feature_importance.xlsx'

        if os.path.exists(excel_file_path):
            # Read the feature importance data from the existing Excel file
            df_feature_importance = pd.read_excel(excel_file_path)
            # Replace underscores with space in the Feature column
            df_feature_importance['Feature'] = df_feature_importance['Feature'].str.replace('_', ' ')
        else:
            if model_name == 'RF':
                # Fit a Random Forest model
                clf = RandomForestClassifier(n_estimators=100, random_state=42)
                # Prepare the data for evaluation
                X = self.data.drop([Constants.COUNTRY, Constants.TARGET_VARIABLE, Constants.SYSTOLIC, Constants.DIASTOLIC], axis=1)
                y = self.data[Constants.TARGET_VARIABLE]
                y = LabelEncoder().fit_transform(y.values.ravel())
                clf.fit(X, y)
                
                # Extract the feature importances from the Random Forest model
                feature_importance_impurity = clf.feature_importances_

                # Initialize the df_feature_importance here for RF
                df_feature_importance = pd.DataFrame({
                    'Feature': X.columns.str.replace('_', ' '),
                    'Mean Decrease in Impurity': feature_importance_impurity,
                    'Feature Permutation Importance': [0]*len(X.columns)  # Assuming default values for permutation importance when model is RF
                })

            else:
                # Load the saved model
                with open(f'{Constants.MODEL_PATH}/global/{model_name}_global.pkl', 'rb') as file:
                    clf = pickle.load(file)
                X = self.data.drop([Constants.COUNTRY, Constants.TARGET_VARIABLE, Constants.SYSTOLIC, Constants.DIASTOLIC], axis=1)
                y = self.data[Constants.TARGET_VARIABLE]
                y = LabelEncoder().fit_transform(y.values.ravel())

                # Evaluate feature importance using mean decrease in impurity
                feature_importance_impurity = clf.feature_importances_

                # Evaluate feature importance using feature permutation importance
                result = permutation_importance(clf, X, y, n_repeats=10, random_state=42)
                feature_importance_permutation = result.importances_mean

                # Create a dataframe of feature importances
                df_feature_importance = pd.DataFrame({
                    'Feature': X.columns.str.replace('_', ' '),
                    'Mean Decrease in Impurity': feature_importance_impurity,
                    'Feature Permutation Importance': feature_importance_permutation
                })

                # Save the feature importance results to an excel file
                df_feature_importance.to_excel(excel_file_path, index=False)

        # Sort the dataframe by mean decrease in impurity
        df_feature_importance.sort_values(by='Mean Decrease in Impurity', ascending=False, inplace=True)

        # Create a bar plot of the mean decrease in impurity
        fig1, ax1 = plt.subplots(figsize=(16, 10))
        df_feature_importance.plot(kind='bar', x='Feature', y='Mean Decrease in Impurity', ax=ax1)
        ax1.set_xlabel('Feature')
        ax1.set_ylabel('Importance')
        ax1.set_title(f'{model_name} - Mean Decrease in Impurity')
        plt.savefig(f'{result_path}/{model_name}_global_mean_decrease_in_impurity.png', bbox_inches='tight')

        # Sort the dataframe by feature permutation importance
        df_feature_importance.sort_values(by='Feature Permutation Importance', ascending=False, inplace=True)

        # Create a bar plot of the feature permutation importance
        fig2, ax2 = plt.subplots(figsize=(16, 10))
        df_feature_importance.plot(kind='bar', x='Feature', y='Feature Permutation Importance', ax=ax2)
        ax2.set_xlabel('Feature')
        ax2.set_ylabel('Importance')
        ax2.set_title(f'{model_name} - Feature Permutation Importance')
        plt.savefig(f'{result_path}/{model_name}_global_feature_importance.png', bbox_inches='tight')
