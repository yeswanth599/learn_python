"""
#Author: Yeswanth
#Date: 2024/04/15
#Learning: matplotlib
#Concept: PlotLabels Practice
"""
import numpy as np
import matplotlib.pyplot as plt


def labels_p():
    x = np.array([10, 40, 20, 70])
    y = np.array([30, 60, 30, 90])

    plt.plot(x, y, 'x-g')
    plt.show()
    plt.xlabel("X Readings")
    plt.ylabel("Y Readings")


if __name__ == "__main__":
    labels_p()
