# Hare krishna

#int
#% = gives remainder

# python considers everything as string by default, so we convert it to int
# x = int(input("Enter your first  number: "))
# y = int(input("Enter your second number: "))
# z = x + y
# print(f"Sum of {x} and {y} is {z}")

#float

x = float(input("Enter your first  number: "))
y = float(input("Enter your second number: "))
# z = round(x + y) # rounding to nearest whole number , it was interesting to see how it works
# print(f"Sum of {x} and {y} is {z :,}") # here writing f is essential as for {variable} to be replaced, it is necessary to use f-string
   

z = (x / y) # division
print(f"Division of {x} and {y} is {z :.2f}") # here we are using f-string and :.2f to round the result to 2


