import csv
import os

#IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
#VITRO_DATA_SRC = 'C:\\Python\Data\\vitro_data.csv'
IGUANA_DATA_SRC = 'D:\\Python\\build_filename\\data\\iguana_data.csv'
VITRO_DATA_SRC = 'D:\\Python\\build_filename\\data\\vitro_data.csv'
RESULTS_SRC = 'D:\\Python\\build_filename\\data\\results.csv'

iguana_data = []
vitro_data = []

with open(IGUANA_DATA_SRC, newline='') as iguanaInput:
	for row in csv.reader(iguanaInput):
		iguana_data.append(row)

with open(VITRO_DATA_SRC, newline='') as vitroInput:
	for row in csv.reader(vitroInput):
		vitro_data.append(row)

with open(RESULTS_SRC, 'w', newline='') as csvfile:
	results = csv.writer(csvfile, delimiter=',')
	for vcode in vitro_data:
		for icode in iguana_data:
			if vcode[0] == icode[0]:
				results.writerow(icode)
