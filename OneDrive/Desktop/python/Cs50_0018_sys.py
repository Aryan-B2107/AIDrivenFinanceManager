# Hare krishna

import sys

# try:
   
# except IndexError:
#     print("Too few arguments")

#use of normal 

# Check for Error
# if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
    # sys.exit("Too many arguments")
# Print name tags   
# print("Hello, my name is", sys.argv[1])
   # try "Aayush Borse" in terminal

#use of slices

if len(sys.argv) < 2:
   sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)   