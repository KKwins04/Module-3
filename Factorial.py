def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''

    if x == 0 or x == 1:
        return 1
    else:
        #Calling function inside a function
        return x * factorial(x-1)
    
#Display result
print(factorial.__doc__)
print("The factorial of 0  is: ", factorial(0))
print("The factorial of 1  is: ", factorial(1))
print("The factorial of 4  is: ", factorial(4))
print("The factorial of 5  is: ", factorial(5))
print("The factorial of 9  is: ", factorial(9))