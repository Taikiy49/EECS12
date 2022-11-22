#inputting the investment/principal, half-yearly compounded interest rate, and half-yearly investment rate.
def main ():
    print ("This program calculates the future value of a 10-year investment.")
    principal = eval(input("Enter the initial investment/principal: "))
    r = eval(input("Enter the half-yearly compounded interest rate (less than 1): "))
    Y = eval(input("Enter the half-yearly investment rate (less than 1): "))
#using the values from the input, the equation is used to calculate the future value of a 10-year investment.
    x = 10
    y_amount = principal * Y
    for i in range (x):
        principal = ((principal * (1 + 0.5 * r ) + y_amount ) * (1 + 0.5 * r)) + y_amount
#calculated investment value from years 1 to 10.  
        print ("The balance after year",i+1,"is",principal)
    print ("The value after 10 years is:",principal)
