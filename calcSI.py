def calcSI(x,y,z):
    Amount=x*((1+(0.01*y))**z)
    return Amount
print(calcSI(10000,3.5,7))