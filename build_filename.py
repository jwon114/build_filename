import csv
import os
import datetime

#IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
#VITRO_DATA_SRC = 'C:\\Python\Data\\vitro_data.csv'
#RESULTS_SRC = 'D:\\Python\\build_filename\\data\\results.csv'
IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
VITRO_DATA_SRC = 'C:\\Python\\Data\\vitro_data.csv'
RESULTS_SRC = 'C:\\Python\\Data\\results.csv'

iguana_data = []
vitro_data = []
iguana_data_keys = []

with open(IGUANA_DATA_SRC, newline='') as iguanaInput:
	for row in csv.reader(iguanaInput):
		iguana_data.append(row)
		iguana_data_keys.append(row[0])

with open(VITRO_DATA_SRC, newline='') as vitroInput:
	for row in csv.reader(vitroInput):
		vitro_data.append(row)

#def checkCount(count):
	#if count > 1:


with open(RESULTS_SRC, 'w', newline='') as csvfile:
	results = csv.writer(csvfile, delimiter=',')
	for vcode in vitro_data:
		count = iguana_data_keys.count(vcode[0])
		if vcode[0] in iguana_data_keys:
			index = iguana_data_keys.index(vcode[0])
			#write to output csv file
			results.writerow(iguana_data[index] + [vcode[1]])
			#re-adjust the lists
			iguana_data.pop(index)
			iguana_data_keys.pop(index)
