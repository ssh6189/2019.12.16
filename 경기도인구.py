import numpy as np
import matplotlib as plt
import csv
import pandas

i = 0

data = []
header = []

f = open("C:/Users/student/Desktop/경기도인구데이터.csv", "r")

for i in range(5):
        data1 = f.readline()
        print(data1)

f.close()


with open("C:/Users/student/Desktop/경기도인구데이터.csv", newline='') as csvfile:

    csvdata = csv.reader(csvfile)

    for row in csvdata:

            if row == 0:
                header = row
            else:
                data = row

arr = np.array(data)

print(header)
print(arr)
