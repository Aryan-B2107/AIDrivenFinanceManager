# Hare krishna

# i = n

#approach 0
# while i < 3:    # while loop
#     print("meow")
#     # i = i - 1 # codes works right to left therefore not i = i
#     i += 1


#approach 1    
# for i in [0, 1, 2]: # for loop with defined values
#     print("meow")
    
# for i in range(3): # for loop for big function
#     print("meow")  


#approach 2 
# for _ in range(1):
#     print("meow")  # if you dont care about naming the the iterativ function use underscore
# print("meow\n" *3, end = "") 

# approach 3   
# while True:
#     n = int(input("Enter your number:"))
#     # if n < 0:
#     #     continue
#     # else:
#     #     break
#     if n > 0:
#         break  


#approach 4      
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter n:"))
        if n > 0:
            break
    return n    
            
    
def meow(n):
    for _ in range(n):
        print("meow") 
main()           