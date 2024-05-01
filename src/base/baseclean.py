import numpy as np
import pandas as pd

from util.constants import Constants
from util.helpers import save_cleaned_data
from util.helpers import draw_multiple_box_plot

class BaseCleaner:
    """
    An interface for cleaning a variable in a CSV dataset.
    """

    EARNING_TYPE = 'c10type'
    EARNINGS = 'c10'

    EARNING_9 = {
        'day_var': 'c9d',
        'week_var': 'c9a',
        'month_var': 'c9b',
        'year_var': 'c9c'
    }

    EARNING_10 = {
        'week_var': 'c10a',
        'month_var': 'c10b',
        'year_var': 'c10c'
    }

    LENGTH_TIME_SMOKING = 't4'
    SMOKING_WEEK = 't4c'
    SMOKING_MONTH = 't4b'
    SMOKING_YEAR = 't4a'

    TAKEN_DIABETES_DRUGS = 'h8'
    TAKEN_DIABETES_DRUGS_INSULIN = 'h8a'
    TAKEN_DIABETES_DRUGS_ORAL = 'h8b'

    HAD_CHOLESTEROL_MEASUREMENT = 'h12'
    HAD_CHOLESTEROL_MEASUREMENT_MEASURED = 'l1a'
    HAD_CHOLESTEROL_MEASUREMENT_RAISED = 'l2a'

    def __init__(self, data):
        """
        Initialize the Preprocessor class with the data.

        Args:
        data (pandas.DataFrame): The data to be preprocessed.
        """
        self.data = data
        self.cleaned_data = pd.DataFrame()

    def clean_country(self, country):
        """
        Set the cleaned country variable to the given value.

        Args:
        country (str): The value to use for the cleaned country variable.
        """
        self.cleaned_data[Constants.COUNTRY] = [country] * self.data.shape[0]

    def clean_category(self, new_var, old_var):
        """
        Clean the categorical variable with the given old name and store it with the given new name.

        Args:
        new_var (str): The name to use for the cleaned variable.
        old_var (str): The name of the variable to clean.
        """
        try:
            self.cleaned_data[new_var] = self.data[old_var]
        except KeyError:
            self.cleaned_data[new_var] = ''

    def clean_numeric(self, new_var, old_var):
        """
        Clean the weight_height variable.

        Parameters:
        new_var (str): the name of the new variable to be created after cleaning
        old_var (str): the name of the old variable to be cleaned

        Returns:
        None
        """
        try:
            self.cleaned_data[new_var] = pd.to_numeric(self.data[old_var], errors='coerce')
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def earnings_per_year(self, new_var, earning_type, earnings, conversion_factor):
        """
        Clean the earnings-per-year variable based on the given earning type and earnings columns.

        Args:
        earning_type (str): The name of the column indicating whether earnings are monthly or yearly.
        earnings (str): The name of the column containing the earnings data.
        conversion_factor (float): Conversion factor to USD.
        """
        try:
            earnings_per_year = np.where(self.data[earning_type].str.lower() == 'month',
                                        self.data[earnings] * 12,
                                        self.data[earnings])
            earnings_per_year = np.where(self.data[earning_type].str.lower().isin(['month', 'year']), earnings_per_year, np.nan)
            self.cleaned_data[new_var] = pd.to_numeric(earnings_per_year, errors='coerce') / conversion_factor
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def earnings_per_year_wks_mth_yr(self, new_var, variables, conversion_factor):
        """
        Compute earnings per year for each row of the input DataFrame.

        Parameters:
        - self: DataFrame
            The input DataFrame.
        - new_var: str
            The name of the new column to be created.
        - variables: dict of {str: str}
            A dictionary containing the variable names for weekly, monthly, and yearly earnings, with keys "week_var",
            "month_var", and "year_var", respectively.
        - conversion_factor: int or float
            A conversion factor to convert earnings to the desired currency.

        Returns:
        - None: This method does not return anything, but it creates a new column in the input DataFrame.
        """
        try:
            earnings_per_year = []
            for _, row in self.data.iterrows():
                earnings = np.nan
                if pd.notna(row.get(variables['week_var'])) and isinstance(row[variables['week_var']], int) and int(row[variables['week_var']]) == row[variables['week_var']]:
                    earnings = int(row[variables['week_var']]) * 52.1429 # weeks to year
                elif pd.notna(row.get(variables['month_var'])) and isinstance(row[variables['month_var']], int) and int(row[variables['month_var']]) == row[variables['month_var']]:
                    earnings = int(row[variables['month_var']]) * 12 # months to year
                elif pd.notna(row.get(variables['day_var'])) and isinstance(row[variables['day_var']], int) and int(row[variables['day_var']]) == row[variables['day_var']]:
                    earnings = int(row[variables['day_var']]) * 365 # day to year
                elif pd.notna(row.get(variables['year_var'])) and isinstance(row[variables['year_var']], int) and int(row[variables['year_var']]) == row[variables['year_var']]:
                    earnings = int(row[variables['year_var']])
                earnings_per_year.append(earnings)

            self.cleaned_data[new_var] = pd.to_numeric(earnings_per_year, errors='coerce') / conversion_factor
        except KeyError:
            self.cleaned_data[new_var] = np.nan


    def number_type_tobacco(self, new_var, tobacco_cols, tobacco_types):
        """
        Clean the tobacco variables and store the maximum value and type in the cleaned_data dictionary.

        Args:
        tobacco_cols (List[str]): The names of the columns containing tobacco data.
        tobacco_types (List[str]): The names of the corresponding tobacco types.
        """
        try:
            number_tobacco = []
            type_tobacco = []

            for _, row in self.data.iterrows():
                tobacco = []
                for col, t_type in zip(tobacco_cols, tobacco_types):
                    if str(row[col]).isdigit():
                        tobacco.append(int(row[col]))
                    else:
                        tobacco.append(0)
                    if f"{col}w" in row and str(row[f"{col}w"]).isdigit():
                        tobacco[-1] = round(int(row[f"{col}w"]) / 7, 0)

                max_tobacco = max(tobacco)
                number_tobacco.append(max_tobacco if max_tobacco != 0 else np.nan)
                type_index = tobacco.index(max_tobacco) if max_tobacco != 0 else 99
                if type_index <= len(tobacco_types) - 1:
                    type_tobacco.append(tobacco_types[type_index])
                else:
                    type_tobacco.append('none')

            self.cleaned_data[new_var['name']] = pd.to_numeric(number_tobacco, errors='coerce')
            self.cleaned_data[new_var['type']] = type_tobacco
        except KeyError:
            self.cleaned_data[new_var['name']] = np.nan
            self.cleaned_data[new_var['type']] = ''

    def length_time_smoking(self, new_var, week_var, month_var, year_var):
        """
        Compute the length of time smoking in years for each row of the input DataFrame.

        Parameters:
        - self: DataFrame
            The input DataFrame.
        - new_var: str
            The name of the new column to be created.
        - week_var: str
            The column name for weekly smoking duration.
        - month_var: str
            The column name for monthly smoking duration.
        - year_var: str
            The column name for yearly smoking duration.

        Returns:
        - None: This method does not return anything, but it creates a new column in the input DataFrame.
        """
        try:
            smoking_duration = []
            for _, row in self.data.iterrows():
                if pd.notna(row[week_var]) and row[week_var].is_integer():
                    duration = int(row[week_var]) / 52.1429 # weeks to year
                elif pd.notna(row[month_var]) and row[month_var].is_integer():
                    duration = int(row[month_var]) / 12 # months to year
                elif pd.notna(row[year_var]) and row[year_var].is_integer():
                    duration = int(row[year_var]) # year
                else:
                    duration = np.nan

                if duration == 77: # convert 77 (don't know) to np.nan
                    duration = np.nan

                smoking_duration.append(duration)

            self.cleaned_data[new_var] = pd.to_numeric(smoking_duration, errors='coerce')
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def age_stopped_smoking(self, new_var, old_var):
        """
        Clean the age-stopped-smoking variable (in weeks) based on the given old variable name.

        Args:
        old_var (str): The name of the column containing the age-stopped-smoking data.
        """
        try:
            age_stopped_smoking = pd.to_numeric(self.data[old_var], errors='coerce')
            age_stopped_smoking = age_stopped_smoking.apply(lambda x: x if x != 77 else np.nan)
            self.cleaned_data[new_var] = age_stopped_smoking
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def smoke_home_workplace(self, new_var, smoke_home, smoke_workplace):
        """
        Clean the smoke-home-workplace variable based on the given smoke-home and smoke-workplace columns.

        Args:
        smoke_home (str): The name of the column indicating whether the participant smokes at home.
        smoke_workplace (str): The name of the column indicating whether the participant smokes at work.
        """
        try:
            smoke_home = pd.to_numeric(self.data[smoke_home], errors='coerce')
            smoke_workplace = pd.to_numeric(self.data[smoke_workplace], errors='coerce')
            smoke_home_workplace = np.where((smoke_home == 1) | (smoke_workplace == 1), 1, 2)
            smoke_home_workplace = np.where((smoke_home.isna()) & (smoke_workplace.isna()), np.nan, smoke_home_workplace)
            self.cleaned_data[new_var] = smoke_home_workplace
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def taken_diabetes_drugs(self, new_var, drugs):
        """
        Check if any diabetes drugs have been taken and create a new column in the DataFrame.

        Parameters:
        - self: DataFrame
            The input DataFrame.
        - new_var: str
            The name of the new column to be created.
        - drugs: list of str
            The column names for diabetes drugs.

        Returns:
        - None: This method does not return anything, but it creates a new column in the input DataFrame.
        """
        try:
            taken_diabetes_drugs = []
            for _, row in self.data.iterrows():
                drugs_taken = 0
                for drug in drugs:
                    if pd.notna(row[drug]) and row[drug].is_integer() and row[drug] != 0:
                        drugs_taken = 1
                        break
                taken_diabetes_drugs.append(drugs_taken)

            self.cleaned_data[new_var] = pd.to_numeric(taken_diabetes_drugs, errors='coerce')
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def had_cholesterol_measurement(self, new_var, measured, raised):
        """
        Check if a cholesterol measurement has been taken and create a new column in the DataFrame.

        Parameters:
        - self: DataFrame
            The input DataFrame.
        - measured: str
            The column name for the cholesterol measurement.
        - raised: str
            The column name for the cholesterol being raised.
        - new_var: str
            The name of the new column to be created.

        Returns:
        - None: This method does not return anything, but it creates a new column in the input DataFrame.
        """
        try:
            had_cholesterol_measurement = []
            for _, row in self.data.iterrows():
                l1a = row.get(measured)
                l2a = row.get(raised)
                if pd.notna(l1a) and l1a.is_integer() and l1a != 2:
                    if pd.notna(l2a) and l2a.is_integer() and l2a != 2:
                        had_cholesterol_measurement.append(1)
                    else:
                        had_cholesterol_measurement.append(1)
                else:
                    had_cholesterol_measurement.append(np.nan)

            self.cleaned_data[new_var] = pd.to_numeric(had_cholesterol_measurement, errors='coerce')
        except KeyError:
            self.cleaned_data[new_var] = ''

    def consumed_alcohol(self, new_var, old_var, has_a_b=False):
        """
        Clean the consumed-alcohol variable based on the given old variable name.

        Args:
        old_var (str): The name of the column containing the consumed-alcohol data.
        """
        try:
            if has_a_b:
                consumed_alcohol = []
                for _, row in self.data.iterrows():
                    a1a = row.get(new_var + 'a')
                    a1b = row.get(new_var + 'b')
                    if pd.notna(a1a) and a1a.is_integer() and a1a != 2:
                        if pd.notna(a1b) and a1b.is_integer() and a1b != 2:
                            consumed_alcohol.append(1)
                        else:
                            consumed_alcohol.append(1)
                    else:
                        consumed_alcohol.append(0)

                self.cleaned_data[new_var] = pd.to_numeric(consumed_alcohol, errors='coerce')
            else:
                self.cleaned_data[new_var] = pd.to_numeric(self.data[old_var], errors='coerce')
        except KeyError:
            self.cleaned_data[new_var] = ''

    def quit_drinking_for_health(self, new_var, old_var):
        """
        Clean the quit-drinking-for-health variable based on the given old variable name.

        Args:
        old_var (str): The name of the column containing the quit-drinking-for-health data.
        """
        try:
            quit_drinking_for_health = pd.to_numeric(self.data[old_var], errors='coerce')
            self.cleaned_data[new_var] = quit_drinking_for_health
        except KeyError:
            self.cleaned_data[new_var] = ''

    def number_alcoholic_drinks(self, new_var, old_var):
        """
        Clean the number-alcoholic-drinks variable based on the given old variable name.

        Args:
        old_var (str): The name of the column containing the number-alcoholic-drinks data.
        """
        try:
            number_alcoholic_drinks = pd.to_numeric(self.data[old_var], errors='coerce')
            self.cleaned_data[new_var] = number_alcoholic_drinks
        except KeyError:
            self.cleaned_data[new_var] = ''

    def number_daily_fruit_vegetables(self, new_var, eat_fruit, fruit_servings, eat_vegetable, vegetable_servings):
        """
        Clean the number-daily-fruit-vegetables variable based on the given columns containing fruit and vegetable data.

        Args:
        eat_fruit (str): The name of the column indicating whether the participant eats fruit.
        fruit_servings (str): The name of the column containing the number of fruit servings.
        eat_vegetable (str): The name of the column indicating whether the participant eats vegetables.
        vegetable_servings (str): The name of the column containing the number of vegetable servings.
        """
        try:
            eat_fruit = pd.to_numeric(self.data[eat_fruit], errors='coerce').fillna(0)
            fruit_servings = pd.to_numeric(self.data[fruit_servings], errors='coerce').fillna(0)
            eat_vegetable = pd.to_numeric(self.data[eat_vegetable], errors='coerce').fillna(0)
            vegetable_servings = pd.to_numeric(self.data[vegetable_servings], errors='coerce').fillna(0)
            number_daily_fruit_vegetables = (eat_fruit * fruit_servings) + (eat_vegetable * vegetable_servings)
            self.cleaned_data[new_var] = number_daily_fruit_vegetables
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def work_intensity(self, new_var, vigorous_intensity, moderate_intensity):
        """
        Clean the work_intensity variable by assigning a label based on the level of work intensity.

        Args:
        vigorous_intensity (str): The column name for vigorous intensity exercise in the original dataset.
        moderate_intensity (str): The column name for moderate intensity exercise in the original dataset.
        """
        try:
            vigorous_intensity = pd.to_numeric(self.data[vigorous_intensity], errors='coerce').fillna(0)
            moderate_intensity = pd.to_numeric(self.data[moderate_intensity], errors='coerce').fillna(0)

            work_intensity = np.where((vigorous_intensity == 1), 'vigorous-intensity',
                                    np.where((moderate_intensity == 1), 'moderate-intensity', 'none'))

            self.cleaned_data[new_var] = work_intensity
        except KeyError:
            self.cleaned_data[new_var] = ''

    def time_walking_bicycling_minutes(self, new_var, time_walking_bicycle_hours, time_walking_bicycle_minutes):
        """
        Clean the time_walking_bicycling_minutes variable by computing the total number of minutes for walking or bicycling.

        Parameters:
        -----------
        time_walking_bicycle_hours: str
            Column name for the hours spent on walking or bicycling.
        time_walking_bicycle_minutes: str
            Column name for the minutes spent on walking or bicycling.

        Returns:
        --------
        None
            The function updates the cleaned_data dictionary by adding the computed total minutes for walking or bicycling
            under the key 'time-walking-bicycling-minutes'.
        """
        try:
            time_walking_bicycling_minutes = pd.to_numeric(self.data[time_walking_bicycle_hours], errors='coerce') * 60 + pd.to_numeric(self.data[time_walking_bicycle_minutes], errors='coerce')
            time_walking_bicycling_minutes = np.where(time_walking_bicycling_minutes.isna(), np.nan, time_walking_bicycling_minutes)
            self.cleaned_data[new_var] = time_walking_bicycling_minutes
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def time_sedentary(self, new_var, sedentary_hours, sedentary_minutes):
        """
        Clean the time_sedentary variable by converting hours and minutes to minutes.

        Parameters:
        hours (str): The name of the column containing the number of hours spent in sedentary activities.
        minutes (str): The name of the column containing the number of minutes spent in sedentary activities.

        Returns:
        None

        The cleaned data is stored in the 'time-sedentary' column of the cleaned_data dataframe.
        """
        try:
            time_sedentary = pd.to_numeric(self.data[sedentary_hours], errors='coerce') * 60 + pd.to_numeric(self.data[sedentary_minutes], errors='coerce')
            time_sedentary = np.where(time_sedentary.isna(), np.nan, time_sedentary)
            self.cleaned_data[new_var] = time_sedentary
        except KeyError:
            self.cleaned_data[new_var] = np.nan

    def run_cleaning(self, properties={}):
        """
        Execute the cleaning job.

        Args:
        data (pandas.DataFrame): The data to be cleaned.
        """
        self.clean_country(self.COUNTRY)
        self.clean_category(Constants.SEX, Constants.SEX)
        self.clean_numeric(Constants.AGE, Constants.AGE)
        self.clean_numeric(Constants.YEARS_AT_SCHOOL, self.YEARS_AT_SCHOOL)
        self.clean_category(Constants.LEVEL_OF_EDUCATION, self.LEVEL_OF_EDUCATION)
        self.clean_category(Constants.MARITAL_STATUS, self.MARITAL_STATUS)
        self.clean_category(Constants.WORK_STATUS, self.WORK_STATUS)
        self.clean_numeric(Constants.PPL_IN_HOUSEHOLD, self.PPL_IN_HOUSEHOLD)
        if properties.get('earnings_c9'):
            self.earnings_per_year_wks_mth_yr(Constants.EARNINGS_PER_YEAR, self.EARNING_9, self.CONVERSION_FACTOR)
        elif properties.get('earnings_c10'):
            self.earnings_per_year_wks_mth_yr(Constants.EARNINGS_PER_YEAR, self.EARNING_10, self.CONVERSION_FACTOR)
        else:
            self.earnings_per_year(Constants.EARNINGS_PER_YEAR, self.EARNING_TYPE, self.EARNINGS, self.CONVERSION_FACTOR)
        self.clean_category(Constants.CURRENTLY_SMOKE_TOBACCO, self.CURRENTLY_SMOKE_TOBACCO)
        self.clean_numeric(Constants.AGE_STARTED_SMOKING, self.AGE_STARTED_SMOKING)
        if properties.get('length_smoking'):
            self.length_time_smoking(Constants.LENGTH_TIME_SMOKING, self.SMOKING_WEEK, self.SMOKING_MONTH, self.SMOKING_YEAR)
        else:
            self.clean_numeric(Constants.LENGTH_TIME_SMOKING, self.LENGTH_TIME_SMOKING)
        self.number_type_tobacco({'name': Constants.NUMBER_TOBACCO, 'type': Constants.TYPE_TOBACCO}, self.TOBACCO_COLS, self.TOBACCO_TYPES)
        self.age_stopped_smoking(Constants.AGE_STOPPED_SMOKING, self.AGE_STOPPED_SMOKING)
        self.smoke_home_workplace(Constants.SMOKE_HOME_WORKPLACE, self.SMOKE_HOME, self.SMOKE_WORKPLACE)
        if properties.get('consumed_alcohol'):
            self.consumed_alcohol(Constants.CONSUMED_ALCOHOL, self.CONSUMED_ALCOHOL, has_a_b=True)
        else:
            self.consumed_alcohol(Constants.CONSUMED_ALCOHOL, self.CONSUMED_ALCOHOL)
        self.quit_drinking_for_health(Constants.QUIT_DRINKING_FOR_HEALTH, self.QUIT_DRINKING_FOR_HEALTH)
        self.number_alcoholic_drinks(Constants.NUMBER_ALCOHOLIC_DRINKS, self.NUMBER_ALCOHOLIC_DRINKS)
        self.number_daily_fruit_vegetables(Constants.NUMBER_DAILY_FRUIT_VEGETABLES, self.EAT_FRUIT, self.FRUIT_SERVINGS, self.EAT_VEGETABLE, self.VEGETABLE_SERVINGS)
        self.clean_category(Constants.SALT_CONSUMPTION, self.SALT_CONSUMPTION)
        self.work_intensity(Constants.WORK_INTENSITY, self.VIGOROUS_INTENSITY, self.MODERATE_INTENSITY)
        self.clean_numeric(Constants.DAYS_VIGOROUS_EXERCISE, self.DAYS_VIGOROUS_EXERCISE)
        self.clean_numeric(Constants.DAYS_MODERATE_EXERCISE, self.DAYS_MODERATE_EXERCISE)
        self.time_walking_bicycling_minutes(Constants.TIME_WALKING_BICYCLING_MINUTES, self.TIME_WALKING_BICYCLE_HOURS, self.TIME_WALKING_BICYCLE_MINUTES)
        self.time_sedentary(Constants.TIME_SEDENTARY, self.TIME_SEDENTARY_HOURS, self.TIME_SEDENTARY_MINUTES)
        self.clean_category(Constants.HAD_BLOOD_PRESSURE_MEASUREMENT, self.HAD_BLOOD_PRESSURE_MEASUREMENT)
        self.clean_category(Constants.TAKEN_DRUGS_FOR_RAISED_BP, self.TAKEN_DRUGS_FOR_RAISED_BP)
        self.clean_category(Constants.HAD_BLOOD_SUGAR_MEASUREMENT, self.HAD_BLOOD_SUGAR_MEASUREMENT)
        if properties.get('taken_diabetes_drugs'):
            self.taken_diabetes_drugs(Constants.TAKEN_DIABETES_DRUGS, properties['taken_diabetes_drugs']['drug_list'])
        else:
            self.clean_category(Constants.TAKEN_DIABETES_DRUGS, self.TAKEN_DIABETES_DRUGS)
        if properties.get('had_cholesterol'):
            self.had_cholesterol_measurement(Constants.HAD_CHOLESTEROL_MEASUREMENT, self.HAD_CHOLESTEROL_MEASUREMENT_MEASURED, self.HAD_CHOLESTEROL_MEASUREMENT_RAISED)
        else:
            self.clean_category(Constants.HAD_CHOLESTEROL_MEASUREMENT, self.HAD_CHOLESTEROL_MEASUREMENT)
        self.clean_category(Constants.TAKEN_CHOLESTEROL_ORAL_TREATMENT, self.TAKEN_CHOLESTEROL_ORAL_TREATMENT)
        self.clean_category(Constants.HAD_HEART_ATTACK, self.HAD_HEART_ATTACK)
        self.clean_category(Constants.TAKING_HEART_DISEASE_MEDICATION, self.TAKING_HEART_DISEASE_MEDICATION)
        self.clean_numeric(Constants.READING1_SYSTOLIC, self.READING1_SYSTOLIC)
        self.clean_numeric(Constants.READING1_DIASTOLIC, self.READING1_DIASTOLIC)
        self.clean_numeric(Constants.READING2_SYSTOLIC, self.READING2_SYSTOLIC)
        self.clean_numeric(Constants.READING2_DIASTOLIC, self.READING2_DIASTOLIC)
        self.clean_numeric(Constants.READING3_SYSTOLIC, self.READING3_SYSTOLIC)
        self.clean_numeric(Constants.READING3_DIASTOLIC, self.READING3_DIASTOLIC)
        self.clean_category(Constants.TREATED_FOR_RAISED_BP, self.TREATED_FOR_RAISED_BP)
        self.clean_category(Constants.ARE_YOU_PREGNANT, self.ARE_YOU_PREGNANT)
        self.clean_numeric(Constants.HEIGHT, self.HEIGHT)
        self.clean_numeric(Constants.WEIGHT, self.WEIGHT)
        self.clean_numeric(Constants.WAIST_CIRCUMFERENCE, self.WAIST_CIRCUMFERENCE)
        self.clean_numeric(Constants.HIP_CIRCUMFERENCE, self.HIP_CIRCUMFERENCE)
        self.clean_numeric(Constants.READING1_BPM, self.READING1_BPM)
        self.clean_numeric(Constants.READING2_BPM, self.READING2_BPM)
        self.clean_numeric(Constants.READING3_BPM, self.READING3_BPM)
        self.clean_numeric(Constants.FASTING_BLOOD_GLUCOSE, self.FASTING_BLOOD_GLUCOSE)
        self.clean_numeric(Constants.TOTAL_CHOLESTEROL, self.TOTAL_CHOLESTEROL)
        self.clean_numeric(Constants.URINARY_SODIUM, self.URINARY_SODIUM)
        self.clean_numeric(Constants.URINARY_CREATININE, self.URINARY_CREATININE)
        self.clean_numeric(Constants.TRIGLYCERIDES, self.TRIGLYCERIDES)
        self.clean_numeric(Constants.HDL_CHOLESTEROL, self.HDL_CHOLESTEROL)

        # saved cleaned csv
        save_cleaned_data(self.cleaned_data, Constants.CLEANED_DATA_FILE_PATH, self.__class__.__name__)

        # draw box plot of numeric variables
        draw_multiple_box_plot(data=self.DATA_LOCATION, variables=Constants.NUMERIC_VARIABLES_PLOT,
                               save_location=self.SAVE_LOCATION, filename=self.FILENAME)
