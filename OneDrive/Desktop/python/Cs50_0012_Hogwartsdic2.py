# hare krishna

students = [
    {"name": "hermione", "house": "Gryffindor", "patronus": "Otter" },
    {"name": "harry", "house": "Gryffindor", "patronus": "stag" },
    {"name": "ron", "house": "Gryffindor", "patronus": "jack Russell terrier" },
    {"name": "Draco", "house": "Slytherin", "patronus": None }
    
     
]

for students in students:
    print(students["name"], students["house"], students["patronus"], sep=", ")