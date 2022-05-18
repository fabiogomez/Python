#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcularMaximoRetorno' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY instruccion as parameter.
#

def calcularMaximoRetorno(instruccions):   
    
    max_sum = [0] * len(instruccions)    
         
    for idx, string in enumerate(instruccions):
        
        x = 0
        y = 0
        tmp_max_sum = 0
        for idx2, step in enumerate(string):
            #acumulate value of every step in x and y
            x, y = getStepValue(x, y, step)
            #calcula de sum of absolute values of steps
            tmp_max_sum = abs(x) + abs(y)
            #save the step with maximun value
            if tmp_max_sum > max_sum[idx]:
                max_sum[idx] = tmp_max_sum
            
    return max_sum
        
# Calculate the move in a plane x, y do it in  every step
def getStepValue(x, y, step):
        
        if step == "U":
            return x, y + 1
        if step == "D":
            return x, y -1
        if step == "L":
            return x - 1 , y
        else:
            return x + 1, y
        
    