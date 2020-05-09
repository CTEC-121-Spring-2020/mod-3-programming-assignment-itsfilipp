# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Filipp Kopytyuk

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""

def coffeeProcessor():

    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50

    # get number of pounds from user
    # 1. changed evaluation into "eval"
    # 2. added in quotation mark at the end of the string
    # 3. added in a parathesis at the end
    quantity = eval(input("How many pounds of coffee would you like to order?"))
    
    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    if quantity <= 10:
        shippingPerPound = .76
    # 4. added in a colon after else statement
    else:
        shippingPerPound = 0      
    
    # Calculate cost of order
    # 5. corrected the spelling of "quantity"
    costOfOrder = (quantity * priceOfCoffee) + (quantity * shippingPerPound) + overHead
    
    # Print result
    # 6. added in a quotation mark in the beginning of string
    print("The cost of the order is:",costOfOrder)

# start the program
# 7. corrected the variable by taking out the word "Go"
coffeeProcessor()