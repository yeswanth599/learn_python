"""
#Author: Yeswanth
#Date: 2024/04/13
#Learning: matplotlib
#Concept: basic plot with different markers
"""

import matplotlib.pyplot as plt
import numpy as np
def marker_display_1():
    y=np.array([3,9,3,6])
    plt.plot(y,'o:r')
    plt.title("plot with o symbol & red dot line")
    plt.show()

def marker_display_2():
    y=np.array([3,9,3,6])
    plt.plot(y,'x-g')
    plt.title("plot with x symbol & green solid line")
    plt.show()

def marker_display_3():
    y=np.array([3,9,3,6])
    plt.plot(y,'*--y')
    plt.title("plot with x symbol & green solid line")
    plt.show()

def marker_display_4():
    y=np.array([3,9,3,6])
    plt.plot(y,'*-.y',ms=20)
    plt.title("plot with x symbol & green solid line")
    plt.show()

if __name__=="__main__":
    marker_display_4()