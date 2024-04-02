# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:50:59 2024

@author: mmimsa
"""

import numpy as np
import matplotlib.pyplot as plt
sf = np.sqrt(5.0)
def line_segments(no_of_segments):
    starts = [(0,0)]
    ends = []
    for j in range(no_of_segments):    
        # region A
        if starts[-1][1]==0 and starts[-1][0]<=(3-sf)/2:
            ends.append((starts[-1][0]+2/(1+sf),1))
        # region B
        elif starts[-1][1]==0 and starts[-1][0]>(3-sf)/2:
            ends.append((1,(1-starts[-1][0])*(1+sf)/2))
        # region C
        elif starts[-1][0]==0:
            ends.append((2*(1-starts[-1][1])/(1+sf),1))        
        # Torus identifications
        # A
        if ends[-1][0]>2/(1+sf) and ends[-1][1]==1:
            starts.append((ends[-1][0],0))
        # B
        elif ends[-1][0]==1:
            starts.append((0,ends[-1][1]))
        # C
        elif ends[-1][0]<=2/(1+sf) and ends[-1][1]==1:
            starts.append((ends[-1][0],0))     
    # delete the final start point (it doesn't have an end to match)
    # so we have equal numbers of starts and ends
    return starts[:-1], ends
plt.show()
s, e = line_segments(35)
plt.show()
# This just plots the line segments
def plot_line_segments(starts,ends):    
    # plt.xlim([0,1])
    # plt.ylim([0,1])
    plt.axes().set_aspect('equal')
    for i in range(len(starts)):
        plt.plot([starts[i][0],ends[i][0]],[starts[i][1],ends[i][1]],'b')
    plt.savefig('line_segments.png')   
    return None
plt.show()
plot_line_segments(s, e)
plt.title("[Python] plot the Forward CAT map", fontsize=10)