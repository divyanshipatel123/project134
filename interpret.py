import pandas as pandas
import matplotlib.pyplot as pyplot
import csv 
data = []
with open("final_gravity.csv" , "r") as f:
    csv_reader = csv.reader(f)
    for rows in csv_reader:
        data.append(rows)
headers = data[0]
planet_data = data[1:]
distance_compatible = []
for row in planet_data:
    if float(row[1].translate({ord(','): None})) <= 100 :
        distance_compatible.append(row)
gravity_dist_compatible = []
for row in distance_compatible:
    if float(row[4]) <= 150  or float(row[4]) >= 350:
        gravity_dist_compatible.append(row)
gravity_compatible = []
for row in planet_data:
    if float(row[4]) <= 150  or float(row[4]) >= 350:
        gravity_compatible.append(row)
print(distance_compatible)
print("is distance compatible   " ,len(distance_compatible))
print("is distance and garvity compatible  ",len(gravity_dist_compatible))
print("is garvity compatible  ",len(gravity_compatible))
with open("compatible.csv" , "w", newline = "" )as f :
    csv_writer  = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(gravity_dist_compatible)

