class CategoricalMapping:
    """
    A class that provides categorical mapping for various variables.
    Attributes:
    - sex: a dictionary that maps various inputs for sex to 'male' or 'female'
    - level-of-education: a dictionary that maps various education levels to categories
    - marital-status: a dictionary that maps various marital status to categories
    - work-status: a dictionary that maps various work status to categories
    - currently-smoke-tobacco: a dictionary that maps various inputs for tobacco smoking to 'yes' or 'no'
    - type-tobacco: a dictionary that maps various types of tobacco products to categories
    - smoke-home-workplace: a dictionary that maps various inputs for smoking at home or workplace to 'yes' or 'no'
    - consumed-alcohol: a dictionary that maps various inputs for alcohol consumption to 'yes' or 'no'
    - quit-drinking-for-health: a dictionary that maps various inputs for quitting alcohol for health reasons to 'yes' or 'no'
    - salt-consumption: a dictionary that maps various levels of salt consumption to categories
    - work-intensity: a dictionary that maps various work intensities to categories
    - had-blood-pressure-measurement: a dictionary that maps various inputs for having had blood pressure measurement to 'yes' or 'no'
    - taken-drugs-for-raised-bp: a dictionary that maps various inputs for taking drugs for raised blood pressure to 'yes' or 'no'
    - had-blood-sugar-measurement: a dictionary that maps various inputs for having had blood sugar measurement to 'yes' or 'no'
    - taken-diabetes-drugs: a dictionary that maps various inputs for taking diabetes drugs to 'yes' or 'no'
    - had-cholesterol-measurement: a dictionary that maps various inputs for having had cholesterol measurement to 'yes' or 'no'
    - taken-cholesterol-oral-treatment: a dictionary that maps various inputs for taking oral treatment for cholesterol to 'yes' or 'no'
    - had-heart-attack: a dictionary that maps various inputs for having had a heart attack to 'yes' or 'no'
    - taking-heart-disease-medication: a dictionary that maps various inputs for taking heart disease medication to 'yes' or 'no'
    - treated-for-raised-bp: a dictionary that maps various inputs for being treated for raised blood pressure to 'yes' or 'no'
    - are-you-pregnant: a dictionary that maps various inputs for pregnancy status to 'yes' or 'no'
    """
    sex: dict = {
        'Men': 'male',
        'men': 'male',
        '1': 'male',
        1: 'male',
        '1.0': 'male',
        1.0: 'male',
        'Women': 'female',
        'women': 'female',
        '2': 'female',
        2: 'female',
        '2.0': 'female',
        2.0: 'female',
        '0': 'female',
        0: 'female'
    }
    level_of_education: dict = {
        1: 'no formal schooling',
        1.0: 'no formal schooling',
        '1': 'no formal schooling',
        '1.0': 'no formal schooling',
        2: 'elementary school',
        2.0: 'elementary school',
        '2': 'elementary school',
        '2.0': 'elementary school',
        3: 'elementary school',
        3.0: 'elementary school',
        '3': 'elementary school',
        '3.0': 'elementary school',
        4: 'high school',
        4.0: 'high school',
        '4': 'high school',
        '4.0': 'high school',
        5: 'high school',
        5.0: 'high school',
        '5': 'high school',
        '5.0': 'high school',
        6: 'tertiary',
        6.0: 'tertiary',
        '6': 'tertiary',
        '6.0': 'tertiary',
        7: 'tertiary',
        7.0: 'tertiary',
        '7': 'tertiary',
        '7.0': 'tertiary',
        88: 'no response',
        88.0: 'no response',
        '88': 'no response',
        '88.0': 'no response',
        0: 'no response',
        '0': 'no response',
        0.0: 'no response',
        '0.0': 'no response',
        77: "no response",
        77.0: "no response",
        '77': "no response",
        '77.0': "no response",
        99: 'no response',
        99.0: 'no response',
        '99': 'no response',
        '99.0': 'no response'
    }
    marital_status: dict = {
        1: 'not married',
        1.0: 'not married',
        '1': 'not married',
        '1.0': 'not married',
        2: 'married',
        2.0: 'married',
        '2': 'married',
        '2.0': 'married',
        3: 'separated',
        3.0: 'separated',
        '3': 'separated',
        '3.0': 'separated',
        4: 'divorced',
        4.0: 'divorced',
        '4': 'divorced',
        '4.0': 'divorced',
        5: 'widowed',
        5.0: 'widowed',
        '5': 'widowed',
        '5.0': 'widowed',
        6: 'cohabitating',
        6.0: 'cohabitating',
        '6': 'cohabitating',
        '6.0': 'cohabitating',
        88: 'no response',
        88.0: 'no response',
        '88': 'no response',
        '88.0': 'no response'
    }
    work_status: dict = {
        1: 'employed',
        1.0: 'employed',
        '1': 'employed',
        '1.0': 'employed',
        2: 'employed',
        2.0: 'employed',
        '2': 'employed',
        '2.0': 'employed',
        3: 'employed',
        3.0: 'employed',
        '3': 'employed',
        '3.0': 'employed',
        4: 'unemployed',
        4.0: 'unemployed',
        '4': 'unemployed',
        '4.0': 'unemployed',
        5: 'student',
        5.0: 'student',
        '5': 'student',
        '5.0': 'student',
        6: 'homemaker',
        6.0: 'homemaker',
        '6': 'homemaker',
        '6.0': 'homemaker',
        7: 'retired',
        7.0: 'retired',
        '7': 'retired',
        '7.0': 'retired',
        8: 'unemployed',
        8.0: 'unemployed',
        '8': 'unemployed',
        '8.0': 'unemployed',
        9: 'unemployed',
        9.0: 'unemployed',
        '9': 'unemployed',
        '9.0': 'unemployed',
        88: 'no response',
        88.0: 'no response',
        '88': 'no response',
        '88.0': 'no response'
    }
    currently_smoke_tobacco: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    type_tobacco: dict = {
        'manufactured cigarettes': 'cigarettes',
        'hand-rolled cigarettes': 'cigarettes',
        'tobacco pipes': 'cigarettes',
        'shisha': 'shisha',
        'cigars, cheroots, cigarillos': 'cigars',
        'Kretek': 'cigarettes',
        'Beedee': 'cigarettes',
        'other tobacco product': 'cigarettes',
        'Bidis': 'cigarettes',
        'kreteks': 'cigarettes',
        'home grown tobacco': 'cigars',
        'Gaya': 'cigars',
        'bidis': 'cigarettes',
        'Hookah/Dhaba': 'shisha'

    }
    smoke_home_workplace: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    consumed_alcohol: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    quit_drinking_for_health: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    salt_consumption: dict = {
        1: 'high',
        1.0: 'high',
        '1': 'high',
        '1.0': 'high',
        2: 'high',
        2.0: 'high',
        '2': 'high',
        '2.0': 'high',
        3: 'normal',
        3.0: 'normal',
        '3': 'normal',
        '3.0': 'normal',
        4: 'low',
        4.0: 'low',
        '4': 'low',
        '4.0': 'low',
        5: 'low',
        5.0: 'low',
        '5': 'low',
        '5.0': 'low',
        77: 'no response',
        77.0: 'no response',
        '77': 'no response',
        '77.0': 'no response'
    }
    work_intensity: dict = {
        'vigorous-intensity': 'vigorous-intensity',
        'moderate-intensity': 'moderate-intensity'
    }
    had_blood_pressure_measurement: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    taken_drugs_for_raised_bp: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    had_blood_sugar_measurement: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    taken_diabetes_drugs: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    had_cholesterol_measurement: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    taken_cholesterol_oral_treatment: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    had_heart_attack: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    taking_heart_disease_medication: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    treated_for_raised_bp: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }
    are_you_pregnant: dict = {
        1: 'yes',
        1.0: 'yes',
        '1': 'yes',
        '1.0': 'yes',
        2: 'no',
        2.0: 'no',
        '2': 'no',
        '2.0': 'no'
    }

    @classmethod
    def get_mappings(cls):
        return {
            'sex': cls.sex,
            'level_of_education': cls.level_of_education,
            'marital_status': cls.marital_status,
            'work_status': cls.work_status,
            'currently_smoke_tobacco': cls.currently_smoke_tobacco,
            'type_tobacco': cls.type_tobacco,
            'smoke_home_workplace': cls.smoke_home_workplace,
            'consumed_alcohol': cls.consumed_alcohol,
            'quit_drinking_for_health': cls.quit_drinking_for_health,
            'salt_consumption': cls.salt_consumption,
            'work_intensity': cls.work_intensity,
            'had_blood_pressure_measurement': cls.had_blood_pressure_measurement,
            'taken_drugs_for_raised_bp': cls.taken_drugs_for_raised_bp,
            'had_blood_sugar_measurement': cls.had_blood_sugar_measurement,
            'taken_diabetes_drugs': cls.taken_diabetes_drugs,
            'had_cholesterol_measurement': cls.had_cholesterol_measurement,
            'taken_cholesterol_oral_treatment': cls.taken_cholesterol_oral_treatment,
            'had_heart_attack': cls.had_heart_attack,
            'taking_heart_disease_medication': cls.taking_heart_disease_medication,
            'treated_for_raised_bp': cls.treated_for_raised_bp,
            'are_you_pregnant': cls.are_you_pregnant
        }