# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 21:19:13 2018

@author: Abdul Rafay
"""

#Problem set 0 MIT 6.0001
#A Very Simple Program: Raising a number to a power and taking a logarithm
# =============================================================================
# Assignment:
#  Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”. 
# =============================================================================
import numpy
x = float(input('Enter number x: '))
y = float(input('Enter number y: '))
z = x**y
print('x raised to the power of y is',z)
t=numpy.log2(x)
print('log base 2 of x is',t)