# Hare krishna

# Syntax Error ----> Solved by you
#print("hello world) ---> write ""
# Value Error ----> when user inputs unexpected value
def main():
    x = get_int()
    print(f"x is {x}")
    
    
    
def get_int():
      while True:
        try: # <----- Try statement
            return int(input("Whats x?"))
    
        except ValueError:
             #print("x is not an integer")
             pass #<--- it is for passing
    
        
            
             
         

main()

