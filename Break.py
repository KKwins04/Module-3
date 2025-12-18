#Take input from user
a = input("Please enter a word: ")

#Program to check break keyword
for i in a: #iteriate for loop
    if (i == 'A') or (i == 'a'): #condition 1 and 2
    #display the result
        print("A is found")
        break #Break statement
    else:
        #Display result
        print("A is not found")
