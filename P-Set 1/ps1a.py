# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 15:57:49 2019

@author: Abdul Rafay
"""

# =============================================================================
# PART A HOUSE HUNTING
# =============================================================================

r = 0.04
current_savings = 0.0
annual_salary = float(input('Please enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Please enter the cost of your dream house:'))
portion_down_payment = 0.25*(total_cost)
monthly_salary = annual_salary/12
months = 0
while current_savings <= portion_down_payment:
    current_savings = current_savings + current_savings*(r/12) + portion_saved*monthly_salary
    months += 1
print('Number of months:', months)