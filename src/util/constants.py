from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier


class Constants:
    """
    A class for storing constant values in the codebase.
    """

    CLEANED_DATA_FILE_PATH = "data/cleaned"
    RAW_DATA_FILE_PATH = "data/raw/**/*.csv"

    COUNTRY = 'country'
    SEX = 'sex'
    AGE = 'age'
    YEARS_AT_SCHOOL = 'years_at_school'
    LEVEL_OF_EDUCATION = 'level_of_education'
    MARITAL_STATUS = 'marital_status'
    WORK_STATUS = 'work_status'
    PPL_IN_HOUSEHOLD = 'ppl_in_household'
    EARNINGS_PER_YEAR = 'earnings_per_year'
    CURRENTLY_SMOKE_TOBACCO = 'currently_smoke_tobacco'
    AGE_STARTED_SMOKING = 'age_started_smoking'
    LENGTH_TIME_SMOKING = 'length_time_smoking'
    NUMBER_TOBACCO = 'number_tobacco'
    TYPE_TOBACCO = 'type_tobacco'
    AGE_STOPPED_SMOKING = 'age_stopped_smoking'
    SMOKE_HOME_WORKPLACE = 'smoke_home_workplace'
    CONSUMED_ALCOHOL = 'consumed_alcohol'
    QUIT_DRINKING_FOR_HEALTH = 'quit_drinking_for_health'
    NUMBER_ALCOHOLIC_DRINKS = 'number_alcoholic_drinks'
    NUMBER_DAILY_FRUIT_VEGETABLES = 'number_daily_fruit_vegetables'
    SALT_CONSUMPTION = 'salt_consumption'
    WORK_INTENSITY = 'work_intensity'
    DAYS_VIGOROUS_EXERCISE = 'days_vigorous_exercise'
    DAYS_MODERATE_EXERCISE = 'days_moderate_exercise'
    TIME_WALKING_BICYCLING_MINUTES = 'time_walking_bicycling_minutes'
    TIME_SEDENTARY = 'time_sedentary'
    HAD_BLOOD_PRESSURE_MEASUREMENT = 'had_blood_pressure_measurement'
    TAKEN_DRUGS_FOR_RAISED_BP = 'taken_drugs_for_raised_bp'
    HAD_BLOOD_SUGAR_MEASUREMENT = 'had_blood_sugar_measurement'
    TAKEN_DIABETES_DRUGS = 'taken_diabetes_drugs'
    HAD_CHOLESTEROL_MEASUREMENT = 'had_cholesterol_measurement'
    TAKEN_CHOLESTEROL_ORAL_TREATMENT = 'taken_cholesterol_oral_treatment'
    HAD_HEART_ATTACK = 'had_heart_attack'
    TAKING_HEART_DISEASE_MEDICATION = 'taking_heart_disease_medication'
    READING1_SYSTOLIC = 'reading1_systolic'
    READING1_DIASTOLIC = 'reading1_diastolic'
    READING2_SYSTOLIC = 'reading2_systolic'
    READING2_DIASTOLIC = 'reading2_diastolic'
    READING3_SYSTOLIC = 'reading3_systolic'
    READING3_DIASTOLIC = 'reading3_diastolic'
    TREATED_FOR_RAISED_BP = 'treated_for_raised_bp'
    ARE_YOU_PREGNANT = 'are_you_pregnant'
    HEIGHT = 'height'
    WEIGHT = 'weight'
    WAIST_CIRCUMFERENCE = 'waist_circumference'
    HIP_CIRCUMFERENCE = 'hip_circumference'
    READING_BPM = 'reading_bpm'
    READING1_BPM = 'reading1_bpm'
    READING2_BPM = 'reading2_bpm'
    READING3_BPM = 'reading3_bpm'
    FASTING_BLOOD_GLUCOSE = 'fasting_blood_glucose'
    TOTAL_CHOLESTEROL = 'total_cholesterol'
    URINARY_SODIUM = 'urinary_sodium'
    URINARY_CREATININE = 'urinary_creatinine'
    TRIGLYCERIDES = 'triglycerides'
    HDL_CHOLESTEROL = 'hdl_cholesterol'
    SYSTOLIC = 'systolic'
    DIASTOLIC = 'diastolic'
    NUMERIC_VARIABLES_PLOT = ['age', 'years_at_school', 'ppl_in_household', 'earnings_per_year', 'age_started_smoking',
                              'length_time_smoking', 'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks',
                              'number_daily_fruit_vegetables', 'days_vigorous_exercise', 'days_moderate_exercise',
                              'time_walking_bicycling_minutes', 'time_sedentary', 'height', 'weight', 'waist_circumference',
                              'hip_circumference', 'fasting_blood_glucose', 'total_cholesterol', 'urinary_sodium', 'urinary_creatinine',
                              'triglycerides', 'hdl_cholesterol']

    NUMERIC_VARIABLES_PLOT_PROCESSING = ['age', 'years_at_school', 'ppl_in_household', 'earnings_per_year', 'age_started_smoking',
                                         'length_time_smoking', 'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks',
                                         'number_daily_fruit_vegetables', 'days_vigorous_exercise', 'days_moderate_exercise',
                                         'time_walking_bicycling_minutes', 'time_sedentary', 'height', 'weight', 'waist_circumference',
                                         'hip_circumference', 'fasting_blood_glucose', 'total_cholesterol', 'urinary_sodium', 'urinary_creatinine',
                                         'triglycerides', 'hdl_cholesterol', 'systolic', 'diastolic', 'reading_bpm']

    PROCESSOR_CATEGORICAL_COLS = ['sex', 'level_of_education', 'marital_status', 'work_status', 'currently_smoke_tobacco',
                                  'type_tobacco', 'smoke_home_workplace', 'consumed_alcohol', 'quit_drinking_for_health',
                                  'salt_consumption', 'work_intensity', 'had_blood_pressure_measurement', 'taken_drugs_for_raised_bp',
                                  'had_blood_sugar_measurement', 'taken_diabetes_drugs', 'had_cholesterol_measurement',
                                  'taken_cholesterol_oral_treatment', 'had_heart_attack', 'taking_heart_disease_medication',
                                  'treated_for_raised_bp', 'are_you_pregnant']

    PROCESSOR_NUMERIC_COLS = ['age', 'years_at_school', 'ppl_in_household', 'earnings_per_year', 'age_started_smoking',
                              'length_time_smoking', 'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks',
                              'number_daily_fruit_vegetables', 'days_vigorous_exercise', 'days_moderate_exercise',
                              'time_walking_bicycling_minutes', 'time_sedentary', 'height', 'weight', 'waist_circumference',
                              'hip_circumference', 'reading1_bpm', 'reading2_bpm', 'reading3_bpm', 'fasting_blood_glucose', 'total_cholesterol', 'urinary_sodium', 'urinary_creatinine', 'triglycerides', 'hdl_cholesterol',
                              'reading1_systolic', 'reading2_systolic', 'reading3_systolic', 'reading1_diastolic', 'reading2_diastolic',
                              'reading3_diastolic']

    MODEL_CATEGORICAL_COLS = PROCESSOR_CATEGORICAL_COLS
    # MODEL_CATEGORICAL_COLS = ['sex', 'level_of_education', 'marital_status', 'work_status', 'currently_smoke_tobacco',
    #                           'smoke_home_workplace', 'consumed_alcohol', 'salt_consumption', 'work_intensity',
    #                           'had_blood_pressure_measurement', 'had_blood_sugar_measurement', 'had_cholesterol_measurement',
    #                           'had_heart_attack', 'taking_heart_disease_medication', 'treated_for_raised_bp', 'are_you_pregnant']

    MODEL_NUMERIC_COLS = ['age', 'years_at_school', 'ppl_in_household', 'earnings_per_year', 'age_started_smoking', 'length_time_smoking',
                          'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks', 'number_daily_fruit_vegetables',
                          'days_vigorous_exercise', 'days_moderate_exercise', 'time_walking_bicycling_minutes', 'time_sedentary',
                          'height', 'weight', 'waist_circumference', 'hip_circumference', 'fasting_blood_glucose', 'total_cholesterol',
                          'urinary_sodium', 'urinary_creatinine', 'triglycerides', 'hdl_cholesterol', 'systolic', 'diastolic', 'reading_bpm']
    # MODEL_NUMERIC_COLS = ['age', 'years_at_school', 'ppl_in_household', 'number_alcoholic_drinks',
    #                       'number_daily_fruit_vegetables', 'days_vigorous_exercise', 'days_moderate_exercise',
    #                       'time_walking_bicycling_minutes', 'time_sedentary', 'height', 'weight', 'waist_circumference',
    #                       'hip_circumference', 'fasting_blood_glucose', 'total_cholesterol', 'triglycerides', 'hdl_cholesterol',
    #                       'systolic', 'diastolic', 'reading_bpm']

    TARGET_VARIABLE = 'blood_pressure'
    SYSTOLIC = 'systolic'
    DIASTOLIC = 'diastolic'

    ANALYZER_PATH = 'data/analyzer'
    HARMONIZER_FILE_PATH = 'data/harmonized/harmonized.csv'
    BASELINE_FILE_PATH = 'data/processed/baseline.csv'
    PROCESSOR_FILE_PATH = 'data/processed/processed.csv'
    PLOT_PATH = 'data/plots'
    MODELLING_FILE_PATH = 'data/modelling'
    GOLD_STANDARD_FILE = 'data/processed/test_gold_standard.csv'

    COLUMNS_TO_DROP = ['reading1_systolic', 'reading1_diastolic', 'reading2_systolic',
                       'reading2_diastolic', 'reading3_systolic', 'reading3_diastolic', 'reading1_bpm',
                       'reading2_bpm', 'reading3_bpm']

    # Define models
    MODELS = {
        'LR': LogisticRegression(max_iter=1000),
        # 'LDA': LinearDiscriminantAnalysis(),
        'KNN': KNeighborsClassifier(),
        # 'CART': DecisionTreeClassifier(),
        # 'NB': GaussianNB(),
        # 'SVM': SVC(),
        # 'AB': AdaBoostClassifier(),
        # 'GBM': GradientBoostingClassifier(),
        'RF': RandomForestClassifier(),
        # 'ET': ExtraTreesClassifier(),
        'XGB': XGBClassifier(),
        # 'MLP': MLPClassifier()
    }

    MODEL_PATH = 'models'
    MODEL_RESULTS = 'results'

    COUNTRIES = ['afghanistan', 'algeria', 'american_samoa', 'armenia', 'azerbaijan', 'bahamas', 'bangladesh', 'barbados', 'belarus', 'benin', 'bhutan', 'botswana', 'british_virgin_islands', 'cayman_islands', 'central_african_republic', 'chad', 'comoros', 'cook_islands', 'cote_divoire', 'democratic_republic_of_the_congo', 'ecuador', 'eritrea', 'eswatini', 'ethiopia', 'fiji', 'french_polynesia', 'gabon', 'gambia', 'georgia', 'ghana', 'grenada', 'guinea',
                 'guyana', 'kiribati', 'kyrgyzstan', 'lao_people_democratic_republic', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'maldives', 'mali', 'mauritania', 'micronesia', 'moldova', 'mongolia', 'mozambique', 'myanmar', 'namibia', 'nauru', 'nepal', 'niger', 'niue', 'palau', 'palestine', 'qatar', 'rwanda', 'samoa', 'sierra_leone', 'solomon_islands', 'sri_lanka', 'tanzania', 'timor-leste', 'togo', 'tokelau', 'tonga', 'tuvalu', 'uganda', 'vanuatu', 'zambia']
    REGIONS = {
        'east_asia_and_pacific': ['american_samoa', 'cook_islands', 'fiji', 'french_polynesia', 'kiribati', 'lao_people_democratic_republic', 'palau',
                                  'micronesia', 'mongolia', 'myanmar', 'nauru', 'niue', 'samoa', 'solomon_islands', 'timor-leste',
                                  'tokelau', 'tonga', 'tuvalu', 'vanuatu'],
        'europe_and_central_asia': ['armenia', 'azerbaijan', 'belarus', 'georgia', 'kyrgyzstan', 'moldova'],
        'latin_america_and_caribbean': ['bahamas', 'barbados', 'british_virgin_islands', 'cayman_islands', 'ecuador', 'grenada', 'guyana'],
        'middle_east_and_north_africa': ['qatar', 'palestine'],
        'south_asia': ['afghanistan', 'bangladesh', 'bhutan', 'maldives', 'nepal', 'sri_lanka'],
        'sub_saharan_africa': ['benin', 'botswana', 'chad', 'comoros', 'cote_divoire', 'democratic_republic_of_the_congo',
                               'eritrea', 'eswatini', 'ethiopia', 'gabon', 'gambia', 'ghana', 'guinea', 'liberia', 'madagascar', 'malawi', 'mali', 'central_african_republic', 'mauritania', 'algeria', 'libya', 'lesotho',
                               'mozambique', 'namibia', 'niger', 'rwanda', 'sierra_leone', 'tanzania', 'togo', 'uganda', 'zambia']
    }

    UPPER_MULTIPLIER = 0.2
    LOWER_MULTIPLIER = 0.05
    OUTLIER_UPPER_WHISKER = ['earnings_per_year', 'length_time_smoking', 'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks', 'number_daily_fruit_vegetables', 'days_vigorous_exercise', 'days_moderate_exercise', 'time_walking_bicycling_minutes', 'fasting_blood_glucose','urinary_sodium', 'urinary_creatinine', 'triglycerides', 'age_started_smoking']
    OUTLIER_LOWER_WHISKER = ['age_started_smoking', 'earnings_per_year', 'length_time_smoking', 'number_tobacco', 'age_stopped_smoking', 'number_alcoholic_drinks','days_vigorous_exercise', 'days_moderate_exercise', 'fasting_blood_glucose','urinary_sodium', 'urinary_creatinine', 'triglycerides', 'hdl_cholesterol']
    CHOLESTEROL_VARS = ['total_cholesterol', 'hdl_cholesterol']
