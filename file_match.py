import os, csv

#IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
#VITRO_DATA_SRC = 'C:\\Python\Data\\vitro_data.csv'
#RESULTS_SRC = 'D:\\Python\\build_filename\\data\\results.csv'
IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
VITRO_DATA_SRC = 'C:\\Python\\Data\\vitro_data.csv'
RESULTS_SRC = 'C:\\Python\\Data\\results.csv'
RESULTS_CHECK = 'C:\\Python\\Data\\results_check.txt'

iguana_data = []
vitro_data = []
iguana_data_keys = []
vitro_data_keys = []

with open(IGUANA_DATA_SRC, newline='') as iguanaInput:
    for row in csv.reader(iguanaInput):
        iguana_data_keys.append(row[0])

with open(VITRO_DATA_SRC, newline='') as vitroInput:
    for row in csv.reader(vitroInput):
        vitro_data_keys.append(row[0])

count = 0
with open(RESULTS_CHECK, 'w') as resultsCheck:
    for v in vitro_data_keys:
        if v in iguana_data_keys:
            resultsCheck.write(v + '\n')            
            count += 1
        
print(count)