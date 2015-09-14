import csv

#Opening file and storing data
file = open('FlightTime(1).csv')
data = csv.reader(file)
cleanData = []

#Cleaning data
for row in data:
	if row[0] == 'Flight Date': #Ignoring first row
		continue
	if row[5] == '' or int(row[9]) < 100: #Ignoring bad data
		continue
	cleanData.append(row) #Appending clean data

#Casting important numbers as integers
for row in cleanData: 
	row[6] = int(row[6])
	row[8] = int(row[8])
	row[9] = int(row[9])

#Recording number of observations
numObsvn = len(cleanData)	

#Calculating target flight time
d, LAMo, LAMd = 1411.13, 33.4342, 41.9786
tft = (.117 * d) + .517 * (LAMo - LAMd) + 43.2

#Calculating average departure and arrival delays
sumDepDelay = 0
sumArvDelay = 0

for row in cleanData:
	sumDepDelay += row[6]
	sumArvDelay += row[8]

avgDepDelay = sumDepDelay / numObsvn
avgArvDelay = sumArvDelay / numObsvn

#Calculating typical time
typT = tft + avgDepDelay + avgArvDelay

#Separating the data by airline
#Defining a function to sort the data by airline

def airlineSort(x): #Where x is the airline code
	y = []
	for row in cleanData:
		if row[1] == x:
			y.append(row)

	return y

AAdata = airlineSort('AA')
F9data = airlineSort('F9')
NKdata = airlineSort('NK')
UAdata = airlineSort('UA')
USdata = airlineSort('US')

#Defining a function to calculate the average flight time of a data set
def avgFltTime(airlineData):
	airlineSum = 0
	for row in airlineData:
		airlineSum += row[9]

	return airlineSum / len(airlineData)

AAavgFltTime = avgFltTime(AAdata)
F9avgFltTime = avgFltTime(F9data)
NKavgFltTime = avgFltTime(NKdata)
UAavgFltTime = avgFltTime(UAdata)
USavgFltTime = avgFltTime(USdata)

#Calculating the time added for each airline
AAtimeAdded = AAavgFltTime - typT
F9timeAdded = F9avgFltTime - typT
NKtimeAdded = NKavgFltTime - typT
UAtimeAdded = UAavgFltTime - typT
UStimeAdded = USavgFltTime - typT

#Finding the fastest airline
#Storing the correlated times in a dictionary
timeAddedDict = {AAtimeAdded:'AA', F9timeAdded:'F9', NKtimeAdded:'NK', UAtimeAdded:'UA', UStimeAdded:'US'}
fastestAirline = timeAddedDict[min(timeAddedDict)]

#Outputing results to a file
outputFile = open('case1.txt', 'a')

outputFile.write('\n')
outputFile.write("The number of observations is: ")
outputFile.write(str(numObsvn))
outputFile.write('\n\n')

outputFile.write("The target flight time of this route is: ")
outputFile.write(str(tft))
outputFile.write(" minutes\n\n")

outputFile.write("The typical time of this route is: ")
outputFile.write(str(typT))
outputFile.write(" minutes\n\n")

outputFile.write("The time added for AA is: ")
outputFile.write(str(AAtimeAdded))
outputFile.write(" minutes\n")

outputFile.write("The time added for F9 is: ")
outputFile.write(str(F9timeAdded))
outputFile.write(" minutes\n")

outputFile.write("The time added for NK is: ")
outputFile.write(str(NKtimeAdded))
outputFile.write(" minutes\n")

outputFile.write("The time added for UA is: ")
outputFile.write(str(UAtimeAdded))
outputFile.write(" minutes\n")

outputFile.write("The time added for US is: ")
outputFile.write(str(UStimeAdded))
outputFile.write(" minutes\n\n")

outputFile.write("The airline with the lowest time added is: ")
outputFile.write(str(fastestAirline))
outputFile.write("\n\n")

outputFile.close()


quit(0)
