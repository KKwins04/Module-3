#define function to calculate cube
def cube(number):
    return number * number * number

#Define a function which will execute cube function if the user entered number is divisible by 3
def by_3(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
    
#Display result
print(by_3(27))
print(by_3(10))
