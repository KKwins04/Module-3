# Take input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Create a list of square values
squares = [i**2 for i in range(start, end + 1)]

# Separate odd and even square values
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Display results
print("Square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
