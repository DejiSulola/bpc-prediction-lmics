# Predicting High Blood Pressure using Machine Learning Models in LMICs

This repository contains the data and code for the research paper "Predicting high blood pressure using machine learning models in low- and middle-income countries" by Ekaba Bisong, Noor Jibril, Preethi Premnath, Elsy Buligwa, George Oboh, and Adanna Chukwuma.

## Dataset

The dataset used in this study is derived from the World Health Organization's STEPwise approach to Surveillance (STEPS) surveys. It includes nationally representative samples of adults aged 18-69 years from 57 low- and middle-income countries (LMICs) spanning six WHO regions.

The dataset contains 184,674 observations and 48 variables, including:
- 11 demographic factors
- 24 behavioral measurements
- 5 physical measurements
- 8 biochemical measurements

The target variable is blood pressure status (normal or high).

### Data Files

- `src/data/raw`: Contains raw country data downloaded from STEPS.
- `src/data/transformation`: Contains notebooks for transforming each country data.
- `src/data/harmonized`: Contains the harmonized dataset used for processing and modelling.

## Data Processing

The data has been processed and harmonized to ensure consistency across countries. This includes:
- Standardizing relevant questions and synchronizing features across countries
- Handling missing values and outliers
- Encoding categorical variables
- Scaling numerical variables
- Creating the target variable based on blood pressure measurements

For more details on the data processing steps, please refer to the Methods section of the research paper.

## Contact

For questions or inquiries related to this dataset or research, please contact the corresponding authors:
- Ekaba Bisong (ekaba.bisong@siliconblast.com)
- Adanna Chukwuma (adc785@mail.harvard.edu)