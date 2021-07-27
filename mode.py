import csv

with open('SOCR-HeightWeight.csv', newline='') as hwf:
    reader = csv.reader(hwf)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(num)

from collections import Counter
data = Counter(newData)
modeRange = {
    '90-100': 0,
    '100-110': 0,
    '110-120': 0,
    '120-130': 0,
    '130-140': 0,
    '140-150': 0,
    '150-160': 0,
    '160-170': 0,
    '170-180': 0
}

for weight, recurring in data.items():
    if 90 < float(weight) < 100:
        modeRange['90-100'] += recurring
    elif 100 < float(weight) < 110:
        modeRange['100-110'] += recurring
    elif 110 < float(weight) < 120:
        modeRange['110-120'] += recurring
    elif 120 < float(weight) < 130:
        modeRange['120-130'] += recurring
    elif 130 < float(weight) < 140:
        modeRange['130-140'] += recurring
    elif 140 < float(weight) < 150:
        modeRange['140-150'] += recurring
    elif 150 < float(weight) < 160:
        modeRange['150-160'] += recurring
    elif 160 < float(weight) < 170:
        modeRange['160-170'] += recurring
    elif 170 < float(weight) < 180:
        modeRange['170-180'] += recurring
        

mode_Range, mode_Recurring = 0,0
for range, recurring in modeRange.items():
    if recurring > mode_Recurring:
        mode_Range, mode_Recurring = [int(range.split('-')[0]),int(range.split('-')[1])], recurring

mode = float((mode_Range[0] + mode_Range[1])/2)
print('Mode is -> ' + str(mode))