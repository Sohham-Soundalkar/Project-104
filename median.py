import csv

with open('SOCR-HeightWeight.csv', newline='') as hwf:
    reader = csv.reader(hwf)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(num)

n = len(newData)
newData.sort()
if n % 2 == 0:
    medianOne = float(newData[n//2])
    medianTwo = float(newData[n//2-1])
    median = (medianOne + medianTwo)/2
else:
    median = newData[n//2]

print('Median is -> ' + str(median))