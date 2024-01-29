{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1fd8cf29-ac4a-48d2-9bee-b50b1aa63db6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "def plot_time_series(df, features, unit, observations=20000):\n",
    "    \"\"\"\n",
    "    Plots specified features from a given unit in a DataFrame.\n",
    "\n",
    "    Parameters:\n",
    "    df (DataFrame): The DataFrame containing the data.\n",
    "    features (list of str): List of column names to plot.\n",
    "    unit (float or int): The unit number to filter the DataFrame.\n",
    "    observations (int): Number of observations to plot. Default is 20000.\n",
    "    \"\"\"\n",
    "    # Filter the DataFrame for the specified unit\n",
    "    unit_df = df[df['unit'] == unit]\n",
    "\n",
    "    # Number of features to plot\n",
    "    num_features = len(features)\n",
    "\n",
    "    # Set up the plot\n",
    "    plt.figure(figsize=(5 * num_features, 5))\n",
    "\n",
    "    # Plot each feature\n",
    "    for i, feature in enumerate(features, 1):\n",
    "        plt.subplot(1, num_features, i)\n",
    "        plt.plot(unit_df[feature][:observations])\n",
    "        plt.title(f'{feature} (Unit {unit})')\n",
    "        plt.xlabel('Observation')\n",
    "        plt.ylabel(feature)\n",
    "\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e48c5f46-9134-46ef-a7d3-482959249587",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
