import math
#user inputs n and k values which will be used in the calculations later.
def main():
    print ("Welcome to the EECS 12 Lucas and Fibonacci convergence experiment!")
    n = eval(input("Please enter N (>2): "))
    k = eval(input("Please enter even K (2<=K<N): "))
    if n < 2:
        return print ("Invalid input: N value must be greater than 2.") 
    if k > n:
        return print ("Invalid input: K value must be less than N.")
    if k < 2:
        return print ("Invalid input: K value must be greater than or equal to 2.")

#defining lucas numbers and using the inputted n value to find lucas terms.
    print ("Lucas terms:")
    def lucas(n):
        if n == 0:
            return 2;
        if n == 1:
            return 1;
        else:
            return lucas(n-1) + lucas(n-2);

    for l in range (n+1):
        
        print ("    ",lucas(l))
    print ("The Nth term of Lucas is:",lucas(n))
    print ("\n")
    
#defining fibonacci numbers and using the inputted n value to find fibonacci terms.
    print ("Fibonacci terms:")
    def fibonacci(n):
        if n == 0:
            return 0;
        if n == 1:
            return 1;
        if n == 2:
            return 1;
        else:
            return fibonacci(n-1) + fibonacci(n-2);
    
    for f in range (n+1):
        
        print ("    ",fibonacci(f))
    print ("The Nth term of Fibonacci is:",fibonacci(n))
    print ("\n")

#golden ratio value.
    golden_ratio = (1+math.sqrt(5)) / 2
    print ("Golden Ratio:",golden_ratio)

#finding Fn-k and Fn+k to solve for the left hand side and Lk and Fn to solve for the right hand side. 
    lefthandside = fibonacci(n-k) + fibonacci(n+k) 
    righthandside = fibonacci(n) * lucas(k)

    print ("Fn-k:", fibonacci(n-k))
    print ("Fn+k:", fibonacci(n+k))
    print ("    Left hand side:", lefthandside)
    print ("Lk:", lucas(k))
    print ("Fn:", fibonacci(n))
    print ("    Right hand side:", righthandside)
    
#finding the error of two consecutive fibonacci terms by using the n value and golden ratio. 
    fibonacci_error = abs((fibonacci(n))/(fibonacci(n-1)) - golden_ratio)
    print ("F_err:",round(fibonacci_error,2))
    
main ()