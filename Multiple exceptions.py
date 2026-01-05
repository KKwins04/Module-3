try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num1
    print("Result is: ", result)
    print("Result is: ", result1)

except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed")
except ValueError:
    print("ValueError: Please enter numerical value")
except NameError as ex:
    print("NameError: The exception is", ex)

except:
    print("Other Error: Some error occured")
finally:
    print("I will execute no matter what happens!")