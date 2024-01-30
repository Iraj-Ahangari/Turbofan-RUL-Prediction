import matplotlib.pyplot as plt
import numpy as np

def plot_time_series(df, features, unit, observations=20000):
    """
    Plots specified features from a given unit in a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    features (list of str): List of column names to plot.
    unit (float or int): The unit number to filter the DataFrame.
    observations (int): Number of observations to plot. Default is 20000.
    """
    # Filter the DataFrame for the specified unit
    unit_df = df[df['unit'] == unit]

    # Number of features to plot
    num_features = len(features)

    # Set up the plot
    plt.figure(figsize=(5 * num_features, 5))

    # Calculate the indices for the 25th, 50th, 75th, and 100th percentiles
    percentiles = [25, 50, 75, 100]
    x_ticks = [int(observations * p / 100) for p in percentiles]

    # Plot each feature
    for i, feature in enumerate(features, 1):
        plt.subplot(1, num_features, i)
        plt.plot(unit_df[feature][:observations])
        plt.title(f'{feature} (Unit {unit})')
        plt.xlabel('Observation')
        plt.ylabel(feature)

        # Set x-axis ticks to the percentiles
        # plt.xticks(x_ticks, labels=[f'{p}%' for p in percentiles])
        plt.xticks([])  # Hides x-axis labels

    plt.tight_layout()
    plt.show()
