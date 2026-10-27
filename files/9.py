import csv

with open("olympics.txt","r") as filename:
    reader = csv.DictReader(filename)
    for row in reader:
        print(row)