"""
#Author: Yeswanth
#Date: 2024/04/13
#Learning: matplotlib
#Concept: basic plot line styles
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_line_styles():
    x1 = np.array([10, 15, 22, 45])
    y1 = np.array([6, 59, 23, 40])
    plt.plot(x1, y1, ls='dotted', c='red',lw=2)
    plt.title("Dotted Style Plot")
    plt.show()


def plot_line_styles2():
    x1 = np.array([10, 15, 22, 45])
    y1 = np.array([6, 59, 23, 40])
    plt.plot(x1, y1, ls='dashed', c='green',lw=2)
    plt.title("Dashed Style Plot")
    plt.show()

if __name__ == "__main__":
    plot_line_styles2()
