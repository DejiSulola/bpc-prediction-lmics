import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class NatureVisualizer:
    def __init__(self, data):
        self.data = data
        sns.set(style="whitegrid", context="paper", font_scale=1.2)

    def create_dataframe(self):
        columns = ['Variables', 'Total Population', 'Train Dataset', 'Test Dataset',
                   'Total Population_sd', 'Train Dataset_sd', 'Test Dataset_sd']
        values = [
            ['Age', 40.06, 40.08, 40.02, 13.27, 13.26, 13.31],
            ['Years at school', 7.6, 7.6, 7.58, 5.33, 5.33, 5.32],
            ['People in household', 3.01, 3.01, 3, 2.02, 2.02, 2.01],
            ['Earnings per year', 1727.08, 1734.25, 1698.52, 1533.97, 1538.65, 1515],
            ['Age started smoking', 18.65, 18.65, 18.63, 1.77, 1.77, 1.78],
            ['Length time smoking', 7.38, 7.34, 7.52, 6.32, 6.33, 6.28],
            ['Number tobacco', 7.62, 7.64, 7.57, 3.55, 3.47, 3.94],
            ['Age stopped smoking', 29.87, 29.87, 29.88, 5.81, 5.82, 5.77],
            ['Number alcoholic drinks', 4.76, 4.75, 4.76, 1.06, 1.06, 1.06],
            ['Number daily fruit vegetables', 10.91, 10.91, 10.91, 6.73, 6.72, 6.75],
            ['Days vigorous exercise', 4.66, 4.66, 4.67, 1.04, 1.04, 1.04],
            ['Days moderate exercise', 5.64, 5.64, 5.64, 1.41, 1.41, 1.41],
            ['Time walking bicycling minutes', 60.23, 60.33, 59.87, 34.33, 34.33, 34.32],
            ['Time sedentary', 206.03, 205.89, 206.57, 172.04, 171.9, 172.59],
            ['Height', 162.12, 162.12, 162.14, 10.29, 10.32, 10.17],
            ['Weight', 66.62, 66.63, 66.59, 17.73, 17.73, 17.7],
            ['Waist circumference', 84.89, 84.87, 84.98, 25.35, 25.13, 26.24],
            ['Hip circumference', 95.89, 95.88, 95.9, 15.71, 15.7, 15.75],
            ['Fasting blood glucose', 39.67, 39.6, 39.94, 37.09, 37.07, 37.17],
            ['Total cholesterol', 76.42, 76.26, 77.06, 72.24, 72.23, 72.29],
            ['Urinary sodium', 121.13, 121.09, 121.29, 32.8, 32.76, 32.95],
            ['Urinary creatinine', 55.04, 55.06, 54.96, 38.3, 38.39, 37.93],
            ['Triglycerides', 84.16, 84.13, 84.29, 23.99, 23.97, 24.08],
            ['Hdl cholesterol', 17.67, 17.62, 17.87, 17.64, 17.64, 17.65],
            ['Systolic', 126.91, 126.91, 126.89, 19.1, 19.09, 19.17],
            ['Diastolic', 80.27, 80.28, 80.22, 11.7, 11.7, 11.71],
            ['Reading bpm', 77.48, 77.48, 77.48, 12.32, 12.31, 12.33]
        ]
        df = pd.DataFrame(values, columns=columns)
        return df

    def plot_bar_chart_al_variables(self, df):
        df_mean = df.melt(id_vars='Variables', value_vars=df.columns[1:4], var_name='Dataset', value_name='Mean')
        df_sd = df.melt(id_vars='Variables', value_vars=df.columns[4:], var_name='Dataset', value_name='SD')
        df_sd['Dataset'] = df_sd['Dataset'].apply(lambda x: x[:-3])

        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Variables', y='Mean', hue='Dataset', data=df_mean, ci=None)
        for i, variable in enumerate(df['Variables']):
            for j, dataset in enumerate(['Total Population', 'Train Dataset', 'Test Dataset']):
                sd = df.loc[i, f'{dataset}_sd']
                x = i - 0.3 + 0.3 * j
                y = df.loc[i, dataset]
                ax.errorbar(x, y, yerr=sd, fmt='none', capsize=3, color='black')

        plt.xticks(rotation=90)
        plt.title('Baseline Characteristics Comparison')
        plt.tight_layout()
        plt.savefig('baseline_characteristics_bar_chart_error_bars.png', dpi=300)
        plt.show()

    def plot_bar_chart(self, df):
        num_rows = int(np.ceil(df.shape[0] / 5))
        ncols = 5
        fig, axes = plt.subplots(nrows=num_rows, ncols=ncols, figsize=(10, 11.69))
        fig.tight_layout(pad=1.5)

        for i, row in df.iterrows():
            ax_row = i // ncols
            ax_col = i % ncols
            ax = axes[ax_row, ax_col]

            x = np.arange(3)
            means = [row['Total Population'], row['Train Dataset'], row['Test Dataset']]
            std_devs = [row['Total Population_sd'], row['Train Dataset_sd'], row['Test Dataset_sd']]
            width = 0.4

            bars = ax.bar(x, means, width, yerr=std_devs, capsize=5, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

            ax.set_xticks(x)
            ax.set_xticklabels(['Total', 'Train', 'Test'], fontsize=9)
            # Set Y-axis label only for the first subplot
            # if i == 0:
            #     ax.set_ylabel('Mean with SD')

            ax.set_title(row['Variables'], fontsize=9)


            for bar in bars:
                height = bar.get_height()
                ax.annotate(
                    f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    fontsize=8
                )

        # Remove unused subplots
        for i in range(df.shape[0], num_rows * ncols):
            ax_row = i // ncols
            ax_col = i % ncols
            fig.delaxes(axes[ax_row, ax_col])

        plt.show()

data = {}  # Add LaTeX table data as a dictionary
visualizer = NatureVisualizer(data)
df = visualizer.create_dataframe()
visualizer.plot_bar_chart(df)
