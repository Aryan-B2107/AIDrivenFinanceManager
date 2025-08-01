#Hare krishna

#str 
name = input("Enter your name:")
first , last = name.split() # splits the name into first and last name
name = name.strip() # Removes white space from str
name = name.capitalize() # Capatilizes first leter
# Say hello to user
print("Hello world", sep=" " ) #sep puts the input name on new line
"""print(f"Hello world", end="")""" #end puts them after a space if they are quoted subsequently
#the f symbol here signifies python that it is special str and it sort of conveys it to format it in a special way used for convinience
print( name)

# Check if the user's name is a palindrome
 