#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by Alberto German Verissimo on April 7, 2022

#Get information from user
first_number =int(input("What is the first number? "))
activity = input("What activity? (+ = * /) ")
second_number = int(input("What is the second number? "))

#Do math
if activity == "+":
    print(first_number + second_number)
if activity == "-":
    print(first_number - second_number)
if activity == "*":
    print(first_number * second_number)
if activity == "/":
    print(first_number / second_number)            
