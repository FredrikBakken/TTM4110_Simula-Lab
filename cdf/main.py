# Script to calculate cumulative distribution function

# Pre-requirements:
# py -3.5 -m pip install pandas
# py -3.5 -m pip install numpy
# py -3.5 -m pip install matplotlib

# Run command:
# py -3.5 main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def run():
    filename = "data.csv"   # Replace with data.csv or data_2.csv
    data_req = pd.read_table(filename, sep=",")
    sorted_values = data_req.apply(lambda x: x.sort_values())

    for col in sorted_values.columns:
        y = np.linspace(0., 1., len(sorted_values[col].dropna()))
        plt.plot(sorted_values[col].dropna(), y)

    plt.show()

    return True


if __name__ == "__main__":
    run()