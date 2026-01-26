try:
    age = int(input("Enter your age: "))

    # Check if age value is valid
    if age < 0 or age > 120:
        print("Wrong age entered. Age should be between 0 and 120.")
    else:
        print("Age entered is correct.")

        # Check even or odd
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Error: Please enter a valid integer value for age.")
