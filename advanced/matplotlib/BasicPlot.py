"""
#Author: Yeswanth
#Date: 2024/04/13
#Learning: matplotlib
#Concept: basic plot with line
"""
import numpy as np
import matplotlib.pyplot as plt


# Basic plot creation with x-axis & y-axis
def basic_plot():
    x_values = np.array([1, 2, 3, 4])
    y_values = np.array([2, 4, 8, 4])
    plt.plot(x_values, y_values)
    plt.title("Yeswanth First Plot")
    plt.show()


# basic plot creation with only input is y-axis
# matplot lib adjust the x-axis based on input y-axis
def basic_plot_y():
    y = np.array([151, 220, 310, 412])
    plt.plot(y)
    plt.title("Second Plot")
    plt.show()


if __name__ == "__main__":
    #basic_plot()
    basic_plot_y()
