    # Hare krishna
    
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")
    # here elif directly stops the program once condition are met
    # and if no condition is met, it will go to the next line.
    # So, this program will print the output only once.

# if x < y or x > y:
#     print(f"{x} is less than or greater than {y}")
# else:
#     print(f"{x} is equal to {y}")

# if x != y:
#     print(f"{x} is not equal to {y}")