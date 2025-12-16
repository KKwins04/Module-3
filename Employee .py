def employee(name):
    print(name)

def salary(exp):
    if exp >= 5:
        return 1000000
    elif exp >= 3:
        return 500000
    elif exp >= 1:
        return 100000
    else:
        return 10000
    
employee("Ram")
a = salary(15)
print("Salary of employee is: ", a)
