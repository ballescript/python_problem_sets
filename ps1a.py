# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:26:46 2019

@author: guest1
"""
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0
r = .04
monthly_salary = annual_salary/12
months = 0

while current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    months += 1

print("Number of months: ", months)