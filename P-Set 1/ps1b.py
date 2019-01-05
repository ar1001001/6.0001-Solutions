# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 15:58:19 2019

@author: Abdul Rafay
"""

# =============================================================================
# PART B SAVING WITH A RAISE
# =============================================================================

r = 0.04
current_savings = 0.0
annual_salary = float(input('Please enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Please enter the cost of your dream house:'))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal:'))

portion_down_payment = 0.25*(total_cost)
months = 0
while current_savings <= portion_down_payment:
    current_savings = current_savings + current_savings*(r/12) + portion_saved*annual_salary/12
    months += 1
    if (months)%6 == 0:
        annual_salary = annual_salary + annual_salary*semi_annual_raise

print('Number of months:', months)