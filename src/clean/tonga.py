from base.baseclean import BaseCleaner

class Tonga(BaseCleaner):
    """
    A concrete implementation of the Preprocessor interface for preprocessing Tonga.
    """

    YEARS_AT_SCHOOL = 'c4'
    LEVEL_OF_EDUCATION = 'c5'
    MARITAL_STATUS = 'c7'
    COUNTRY = 'tonga'
    SEX = 'sex'
    AGE = 'age'
    YEARS_AT_SCHOOL = 'c4'
    LEVEL_OF_EDUCATION = 'c5'
    WORK_STATUS = 'c8'
    PPL_IN_HOUSEHOLD = 'c9'
    EARNING_TYPE = 'c10type'
    EARNINGS = 'c10'
    CONVERSION_FACTOR = 2.33236
    CURRENTLY_SMOKE_TOBACCO = 't1'
    AGE_STARTED_SMOKING = 't3'
    TOBACCO_COLS = ['t5a', 't5b', 't5c', 't5d', 't5e', 't5f']
    TOBACCO_TYPES = ['manufactured cigarettes', 'hand-rolled cigarettes', 'tobacco pipes','cigars, cheroots, cigarillos', 'shisha', 'other tobacco product']
    AGE_STOPPED_SMOKING = 't10'
    SMOKE_HOME = 't17'
    SMOKE_WORKPLACE = 't18'
    CONSUMED_ALCOHOL = 'a1'
    QUIT_DRINKING_FOR_HEALTH = 'a3'
    NUMBER_ALCOHOLIC_DRINKS = 'a4'
    EAT_FRUIT = 'd1'
    FRUIT_SERVINGS = 'd2'
    EAT_VEGETABLE = 'd3'
    VEGETABLE_SERVINGS = 'd4'
    SALT_CONSUMPTION = 'd8'
    VIGOROUS_INTENSITY = 'p1'
    MODERATE_INTENSITY = 'p4'
    DAYS_VIGOROUS_EXERCISE = 'p2'
    DAYS_MODERATE_EXERCISE = 'p5'
    TIME_WALKING_BICYCLE_HOURS = 'p9a'
    TIME_WALKING_BICYCLE_MINUTES = 'p9b'
    TIME_SEDENTARY_HOURS = 'p16a'
    TIME_SEDENTARY_MINUTES = 'p16b'
    HAD_BLOOD_PRESSURE_MEASUREMENT = 'h1'
    TAKEN_DRUGS_FOR_RAISED_BP = 'h3'
    HAD_BLOOD_SUGAR_MEASUREMENT = 'h6'
    TAKEN_CHOLESTEROL_ORAL_TREATMENT = 'h14'
    HAD_HEART_ATTACK = 'h17'
    TAKING_HEART_DISEASE_MEDICATION = 'h18'
    READING1_SYSTOLIC = 'm4a'
    READING1_DIASTOLIC = 'm4b'
    READING2_SYSTOLIC = 'm5a'
    READING2_DIASTOLIC = 'm5b'
    READING3_SYSTOLIC = 'm6a'
    READING3_DIASTOLIC = 'm6b'
    TREATED_FOR_RAISED_BP = 'm7'
    ARE_YOU_PREGNANT = 'm8'
    HEIGHT = 'm11'
    WEIGHT = 'm12'
    WAIST_CIRCUMFERENCE = 'm14'
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

    SAVE_LOCATION = 'data/plots/tonga'
    DATA_LOCATION = 'data/cleaned/tonga.csv'
    FILENAME = 'tonga.png'

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
        properties = {'length_smoking': True}
        super().run_cleaning(properties)