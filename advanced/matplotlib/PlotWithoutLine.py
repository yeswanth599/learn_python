"""
#Author: Yeswanth
#Date: 2024/04/13
#Learning: matplotlib
#Concept: basic plot without line
"""

#importing matplotlib to draw plot
import matplotlib.pyplot as plt
#importing numpy array to crate array
import numpy as np

def plot_without_line():
    x=np.array([1,2,3,4])
    y=np.array([3,5,8,12])
    plt.title("Plot Without Line")
    plt.plot(x,y,'x')
    plt.show()

if __name__=="__main__":
    plot_without_line()
