# Hare krishna

def main():
    x = int(input("whats the first number? "))
    print("x squared is ", square(x)) # This will print the squared value

def square(n): # This function squares the given number
#  return pow(n, 2) # Python's built-in pow function is used to calculate the square
   return n * n

if __name__ == "__main__":
    
  main()