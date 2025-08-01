# Hare krishna

#List

students = ["Hermione", "Harry", "Ron"]


#approaach 1
# print(students[1])


#approach 2 
# for students in students:
#     print(students) 

#approach 3
for i in range(len(students)):
    print(i + 1, students[i])

#approach 4 using dictionary

students1 = houses = { "Hermione": "Gryffindor",
                      "Harry": "Gryffindor", 
                      "Ron": "Gryffindor", 
                      "Draco": "Slytherin",
                      }
# print(students1["Hermione"])
for student1 in students1:
    print(student1, students1[student1], sep=", ")
       
    