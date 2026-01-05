valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        #Enter an even number
        while n%2 == 0:
            print("Bye")
            valid = True
            break

    except ValueError:
        print("Invalid!")