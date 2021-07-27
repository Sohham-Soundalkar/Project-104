import csv
with open('SOCR-HeightWeight.csv', newline='') as hwf:
    reader = csv.reader(hwf)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

a = len(newData)
total = 0
for j in newData:
    total += j
mean = total/a

print('Mean (Average) is -> ' + str(mean))