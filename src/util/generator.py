import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class BoxPlotGenerator:
    """
    A class to generate box plots for a given dataset.

    Attributes:
    -----------
    data_path : str
        The path to the dataset
    data : pd.DataFrame
        The dataset

    Methods:
    --------
    load_data():
        Loads the dataset
    draw_box_plots(variables, save_path=None):
        Generates box plots for each variable in variables
        variables : list
            A list of variables to plot
        save_path : str, optional
            The path to save the plot image. Default is None.
        filename : str, optional
            The name of the file to save the plot. Default is 'box_plots.png'.
        title : str, optional
            The title for the plot. Default is None.
    """

    NUM_COLS = 4
    FIGSIZE_X = 25 # 15
    FIGSIZE_Y = 5 # 5

    def __init__(self, data_path = None, data = None):
        self.data_path = data_path
        self.data = data

    def load_data(self):
        """
        Loads the dataset
        """
        if self.data_path is None:
            raise ValueError("data_path is None. Please set it to a valid file path before calling load_data.")
        self.data = pd.read_csv(self.data_path, low_memory=False)

    def draw_box_plots_multiple(self, variables, save_path=None, filename=None, title=None):
        """
        Generates box plots for each variable in variables
        variables : list
            A list of variables to plot
        save_path : str, optional
            The path to save the plot image. Default is None.
        filename : str, optional
            The name of the file to save the plot. Default is 'box_plots.png'.
        title : str, optional
            The title for the plot. Default is None
        """
        if type(self.data) is not pd.DataFrame:
            self.load_data()

        sns.set(style="ticks", font_scale=1.5)

        # Calculate number of rows and columns for subplots
        num_plots = len(variables)
        num_cols = min(self.NUM_COLS, num_plots)
        num_rows = (num_plots + num_cols - 1) // num_cols

        # Create subplots
        fig, axes = plt.subplots(num_rows, num_cols, figsize=(self.FIGSIZE_X, self.FIGSIZE_Y*num_rows), sharey=True)

        # Flatten axes array if it has multiple rows
        if num_rows > 1:
            axes = axes.flatten()

        # Set title
        if title is not None:
            plt.suptitle(title, fontsize=20)

        # Generate box plots for each variable
        for i, var in enumerate(variables):
            sns.boxplot(x=var, data=self.data, color='white', ax=axes[i], showfliers=False)
            sns.stripplot(x=var, data=self.data, jitter=True, size=6, linewidth=0.5, ax=axes[i])

            quartile1, quartile3 = self.data[var].quantile([0.25, 0.75])
            iqr = quartile3 - quartile1
            axes[i].annotate('', xy=(quartile1, 1.02), xytext=(quartile3, 1.02),
                             arrowprops=dict(arrowstyle='|-|', lw=1.5, color='grey'), va='center')
            axes[i].annotate(f'IQR={iqr:.2f}', xy=(quartile1 + iqr/2, 1.03), ha='center', color='grey')

            axes[i].set_xlabel(var.replace('_', ' ').title())
            axes[i].set_ylabel('Value')

            # Add interquartile range text
            textstr = f"IQR: {iqr:.2f}\nQ1: {quartile1:.2f}\nQ3: {quartile3:.2f}"
            axes[i].text(0.95, 0.95, textstr, transform=axes[i].transAxes, fontsize=12,
                         verticalalignment='top', horizontalalignment='right')

            axes[i].yaxis.grid(True)
            # sns.despine(trim=True, left=True)

        # Save figure
        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            name = 'box_plots.png'
            if filename:
                name = filename

            plt.savefig(f'{save_path}/{name}', dpi=300, bbox_inches='tight')

        plt.close()

    def draw_box_plots_single_1(self, variable, save_path=None):
        """
        Create and save a box plot of a single variable from a dataset.
        :param data: Pandas DataFrame containing the dataset
        :param variable: Name of the variable in the dataset to be plotted
        :param save_path: (optional) File path to save the plot
        """
        if self.data is None:
            self.load_data()

        sns.set(style="ticks", font_scale=1.5)
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.boxplot(x=variable, data=self.data, color='white', ax=ax, showfliers=False)
        sns.stripplot(x=variable, data=self.data, jitter=True, size=6, linewidth=0.5, ax=ax)

        quartile1, quartile3 = self.data[variable].quantile([0.25, 0.75])
        iqr = quartile3 - quartile1
        ax.annotate('', xy=(quartile1, 1.02), xytext=(quartile3, 1.02),
                    arrowprops=dict(arrowstyle='|-|', lw=1.5, color='grey'), va='center')
        ax.annotate(f'IQR={iqr:.2f}', xy=(quartile1 + iqr/2, 1.03), ha='center', color='grey')

        ax.set_xlabel(variable.replace('_', ' ').title())
        ax.set_ylabel('Value')

        # Add interquartile range text
        textstr = f"IQR: {iqr:.2f}\nQ1: {quartile1:.2f}\nQ3: {quartile3:.2f}"
        ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='right')

        ax.yaxis.grid(True)
        sns.despine(trim=True, left=True)

        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            plt.savefig(f'{save_path}/{variable}.png', dpi=500, bbox_inches='tight')

        plt.close()

    def draw_box_plots_single_2(self, variable, save_path=None):
        """
        Create and save a box plot of a single variable from a dataset.
        :param data: Pandas DataFrame containing the dataset
        :param variable: Name of the variable in the dataset to be plotted
        :param save_path: (optional) File path to save the plot
        """
        if self.data is None:
            self.load_data()

        # Create the box plot
        fig, ax = plt.subplots(figsize=(8,6))
        sns.set_style('whitegrid')
        sns.boxplot(x=self.data[variable], ax=ax, color='gray')
        ax.set_xlabel(variable.replace('_', ' ').title(), fontsize=14)
        ax.set_ylabel('Value', fontsize=14)
        ax.tick_params(labelsize=12)
        sns.despine()

        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            plt.savefig(f'{save_path}/{variable}.png', dpi=500, bbox_inches='tight')

        plt.close()
