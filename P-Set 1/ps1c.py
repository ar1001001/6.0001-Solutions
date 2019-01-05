# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 15:58:40 2019

@author: Abdul Rafay
"""

# =============================================================================
# PART C FINDING THE RIGHT AMOUNT TO SAVE AWAY
# =============================================================================

r = 0.04

annual_salary = float(input('Please enter your annual salary:'))
y = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25*(total_cost)
months = 36
eps = 50
nosteps = 0
low = 0
high = 10000

while True:
    mid = (low+high)//2
    current_savings = 0
    annual_salary = y
    for i in range(0, months):
        current_savings = current_savings + (annual_salary/12) * mid / 10000 + (current_savings * 0.04) / 12
        if i % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if abs(current_savings - portion_down_payment) <= eps:
        print('Best savings rate: ',  (mid / 10000))
        print('Steps in bisection search: ', nosteps)
        break
    elif abs(current_savings - portion_down_payment) > eps and current_savings > portion_down_payment:
        high = mid
    elif abs(current_savings - portion_down_payment) > eps and current_savings < portion_down_payment:
        low = mid
    if low == high:
        print('It is not possible to pay the down payment in three years.')
        break   
    nosteps += 1
    