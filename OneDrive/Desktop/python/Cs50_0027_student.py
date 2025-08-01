# Hare krsna

import csv


name = input("What's your name?")
home = input("where's your home?")


with open("student.csv", "a") as file:
    writer = csv.DictReader(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})