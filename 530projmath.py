import matplotlib.pyplot as plt
import numpy as np


dataTable = []

def readStuff():
	filename = "examplefile1.txt"
	f = open(filename)

	for line in f:
		list = line.split(",")
		dataTable.append(list)

	rows, cols = (len(dataTable), len(dataTable[0]))

	sumScore = 0 #0-4
	sumGuess = 0 #bits
	sumTime = 0 #seconds
	sumFastHash = 0
	sumNoThrot = 0

	maxScore = 0
	minScore = 4

	maxGuess = 0
	minGuess = float('inf')

	maxTime = 0
	minTime= float('inf')
	
	maxFastHash = 0
	minFastHash = float('inf')

	maxNoThrot = 0
	minNoThrot = float('inf')

	for i in range(rows):
		row = dataTable[i]
		a = int(row[0])
		sumScore += a
		if(a > maxScore):
				maxScore = a
		if(a < minScore):
				minScore = a

		b = float(row[1])
		sumGuess += b
		if(b > maxGuess):
				maxGuess = b
		if(b < minGuess):
				minGuess = b

		c = float(row[2])
		sumTime += c
		if(c > maxTime):
				maxTime = c
		if(c < minTime):
				minTime = c
		
		d = float(row[3])
		sumFastHash += d
		if(d > maxFastHash):
				maxFastHash = d
		if(d < minFastHash):
				minFastHash = d

		e = float(row[4])
		sumNoThrot += e
		if(e > maxNoThrot):
				maxNoThrot = e
		if(e < minNoThrot):
				minNoThrot = e

	avgScore = sumScore/rows
	avgGuess = sumGuess/rows
	avgTime = sumTime/rows
	avgFastHash = sumFastHash/rows
	avgNoThrot = sumNoThrot/rows

	thisdict = {

		"Max Score" : maxScore,
		"Min Score" : minScore,
		"Avg. Score" : avgScore,
		"Max Guesses" : maxGuess,
		"Min Guesses" : minGuess,
		"Avg. Guesses" : avgGuess,
		"Max Time" : maxTime,
		"Min Time" : minTime,
		"Avg. Time" : avgTime,
		"Max FastHash" : maxFastHash,
		"Min FastHash" : minFastHash,
		"Avg FastHash" : avgFastHash,
		"Max NoThrot" : maxNoThrot,
		"Min NoThrot" :	minNoThrot,
		"Avg NoThrot" : avgNoThrot

	}

	plt.figure(1)
	keys = ["Max Score","Min Score","Avg. Score"]
	values = [thisdict.get('Max Score'),thisdict.get('Min Score'),thisdict.get('Avg. Score')]
	plt.bar(keys, values)
	plt.savefig("USandUK-US-score.png")

	plt.figure(2)
	keys2 = ["Max Guesses","Min Guesses","Avg. Guesses"]
	values2 = [thisdict.get('Max Guesses'),thisdict.get('Min Guesses'),thisdict.get('Avg. Guesses')]
	plt.bar(keys2, values2)
	plt.savefig("USandUK-US-guess.png")

	plt.figure(3)
	keys3 = ["Max Time","Min Time","Avg. Time"]
	values3 = [thisdict.get('Max Time'),thisdict.get('Min Time'),thisdict.get('Avg. Time')]
	plt.bar(keys3, values3)
	plt.savefig("USandUK-US-time.png")


	o = open("examplefile1-values", "w")
	o.write(str(thisdict))

	print(thisdict)

def main():
	readStuff()

main()
