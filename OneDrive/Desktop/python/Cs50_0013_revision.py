
# Hare krishna 

# making calculator which takes users name and greets them while it calculates for user and gives grade
def get_name():
    name = input("Enter your name: ")
    return name

def hello():
    name = get_name()
    print("Hello", name)

def basic_calculation():
    hello()

    

    x = float(input("Enter your number X: "))    
    y = float(input("Enter your number Y: ")) 
    print("Enter your choice:\n"
          "1. Sum\n"
          "2. Sub\n"
          "3. Multi\n"
          "4. Div\n"
          "5. Grade\n") 
    choice = int(input("(1-5), enter your choice: "))  

    match choice:
        case 1:
            print("Sum:", x + y)
        case 2:
            print("Sub:", x - y)
        case 3:
            print("Multi:", x * y)  # Corrected from x + y
        case 4:
            if y != 0:
                print("Div:", x / y)
            else:
                print("Error: Division by zero")
        case 5:
            avg = (x + y) / 2
            if avg >= 90:
                grade = 'A'
            elif avg >= 75:
                grade = 'B'
            elif avg >= 60:
                grade = 'C'
            elif avg >= 40:
                grade = 'D'
            else:
                grade = 'F'
            print("Grade:", grade)
        case _:
            print("Invalid choice")

# Run the program
basic_calculation()
            
              

            
        
    

    



