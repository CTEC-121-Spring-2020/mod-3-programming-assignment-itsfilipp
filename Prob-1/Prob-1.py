# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Filipp Kopytyuk

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    if orderSubTotal >= 10:
        shippingCost = 0.0

    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(11.0))
    

if __name__ == "__main__":
    unitTest()