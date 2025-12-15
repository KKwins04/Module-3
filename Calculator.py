def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

#Take input from user
print("Please select an operator")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice=input("Please enter choice (a/b/c/d): ")

num_1= int(input('Please enter first number: '))
num_2= int(input('Please enter second number: '))

if choice == 'a':
    print(num_1,'+',num_2, '=', add(num_1, num_2))
elif choice == 'b':
    print(num_1,'-',num_2, '=', subtract(num_1, num_2))
elif choice == 'c':
    print(num_1,'*',num_2, '=', multiply(num_1, num_2))
elif choice == 'd':
    print(num_1,'/',num_2, '=', divide(num_1, num_2))
else:
    print("Invalid input!")