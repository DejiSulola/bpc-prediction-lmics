from base.baseclean import BaseCleaner

class Maldives(BaseCleaner):
    """
    A concrete implementation of the Preprocessor interface for preprocessing Maldives.
    """

    YEARS_AT_SCHOOL = 'c4'
    LEVEL_OF_EDUCATION = 'c5'
    MARITAL_STATUS = 'c7'
    COUNTRY = 'maldives'
    SEX = 'sex'
    AGE = 'age'
    YEARS_AT_SCHOOL = 'c4'
    LEVEL_OF_EDUCATION = 'c5'
    WORK_STATUS = 'c8'
    PPL_IN_HOUSEHOLD = 'c9'
    EARNING_TYPE = 'c10type'
    EARNINGS = 'c10'
    CONVERSION_FACTOR = 15.4253
    CURRENTLY_SMOKE_TOBACCO = 't1'
    AGE_STARTED_SMOKING = 't3'
    TOBACCO_COLS = ['t5a', 't5b', 't5c', 't5d', 't5e', 't5f']
    TOBACCO_TYPES = ['manufactured cigarettes', 'hand-rolled cigarettes', 'tobacco pipes','cigars, cheroots, cigarillos', 'shisha', 'other tobacco product']
    AGE_STOPPED_SMOKING = 't7'
    SMOKE_HOME = 't119'
    SMOKE_WORKPLACE = 't22'
    CONSUMED_ALCOHOL = 'a1a'
    QUIT_DRINKING_FOR_HEALTH = ''
    NUMBER_ALCOHOLIC_DRINKS = 'a2'
    EAT_FRUIT = 'd1'
    FRUIT_SERVINGS = 'd2'
    EAT_VEGETABLE = 'd3'
    VEGETABLE_SERVINGS = 'd4'
    SALT_CONSUMPTION = ''
    VIGOROUS_INTENSITY = 'p1'
    MODERATE_INTENSITY = 'p4'
    DAYS_VIGOROUS_EXERCISE = 'p2'
    DAYS_MODERATE_EXERCISE = 'p5'
    TIME_WALKING_BICYCLE_HOURS = 'p9a'
    TIME_WALKING_BICYCLE_MINUTES = 'p9b'
    TIME_SEDENTARY_HOURS = 'p16a'
    TIME_SEDENTARY_MINUTES = 'p16b'
    HAD_BLOOD_PRESSURE_MEASUREMENT = 'h1'
    TAKEN_DRUGS_FOR_RAISED_BP = 'h3a'
    HAD_BLOOD_SUGAR_MEASUREMENT = 'h6'
    TAKEN_CHOLESTEROL_ORAL_TREATMENT = 'h14'
    HAD_HEART_ATTACK = 'h17'
    TAKING_HEART_DISEASE_MEDICATION = 'h18'
    READING1_SYSTOLIC = 'm11a'
    READING1_DIASTOLIC = 'm11b'
    READING2_SYSTOLIC = 'm12a'
    READING2_DIASTOLIC = 'm12b'
    READING3_SYSTOLIC = 'm13a'
    READING3_DIASTOLIC = 'm13b'
    TREATED_FOR_RAISED_BP = 'm14'
    ARE_YOU_PREGNANT = 'm5'
    HEIGHT = 'm3'
    WEIGHT = 'm4'
    WAIST_CIRCUMFERENCE = 'm7'
    HIP_CIRCUMFERENCE = 'm15'
    READING1_BPM = 'm16a'
    READING2_BPM = 'm16b'
    READING3_BPM = 'm16c'
    FASTING_BLOOD_GLUCOSE = 'b5' # mg/dL
    TOTAL_CHOLESTEROL = 'b8'    # mg/dL
    URINARY_SODIUM = 'b14'      # mg/dL
    URINARY_CREATININE = 'b15'  # mg/dL
    TRIGLYCERIDES = 'b16'
    HDL_CHOLESTEROL = 'b17'

    SAVE_LOCATION = 'data/plots/maldives'
    DATA_LOCATION = 'data/cleaned/maldives.csv'
    FILENAME = 'maldives.png'

    def __init__(self, data):
        """
        Initialize the class with the data.

        Args:
        data (pandas.DataFrame): The data to be preprocessed.
        """
        super().__init__(data)
        self.run_cleaning()

    def run_cleaning(self):
        """
        Execute the cleaning job.

        Args:
        data (pandas.DataFrame): The data to be cleaned.
        """
        properties = {'earnings_c10': True,
                      'length_smoking': True,
                      'taken_diabetes_drugs': {'drug_list': [self.TAKEN_DIABETES_DRUGS_INSULIN,
                                  self.TAKEN_DIABETES_DRUGS_ORAL]}}
        super().run_cleaning(properties)