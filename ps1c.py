# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:19:29 2019

@author: guest1
"""
annual_salary = int(input("Enter starting salary: "))
semi_annual_raise = .07
r = .04
total_cost = 1000000
portion_down_payment = .25
down_payment = total_cost*portion_down_payment
high = 1
low = 0
rate = (high+low)/2
epsilon = 100
numGuesses = 0

def saved_in_36_months(annual_salary, rate):
    total = 0
    for month in range(0,36):
        total *= 1+(r/12)
        if month%6 == 0 and month > 0:
            annual_salary *= (1+semi_annual_raise)
        total += annual_salary/12*rate  
    return(total)    

while abs(saved_in_36_months(annual_salary, rate) - down_payment) >= epsilon:
    numGuesses += 1
    if saved_in_36_months(annual_salary, rate) < down_payment:
        low = rate
    else:
        high = rate
    rate = (high+low)/2
    if numGuesses >= 42:
        print("It is not possible to pay the down payment in three years.")
        break
    
if numGuesses < 42:
    print("Best savings rate: ", rate)
    print("Steps in bisection search: ", numGuesses)