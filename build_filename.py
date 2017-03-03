import csv, os
from datetime import datetime, timedelta
import pytz

#IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
#VITRO_DATA_SRC = 'C:\\Python\Data\\vitro_data.csv'
#RESULTS_SRC = 'D:\\Python\\build_filename\\data\\results.csv'
IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
VITRO_DATA_SRC = 'C:\\Python\\Data\\vitro_data.csv'
RESULTS_SRC = 'C:\\Python\\Data\\results.csv'

iguana_data = []
vitro_data = []
iguana_data_keys = []
vitro_data_keys = []
local_tz = pytz.timezone('Australia/Sydney')

with open(IGUANA_DATA_SRC, newline='') as iguanaInput:
	for row in csv.reader(iguanaInput):
		iguana_data.append(row)
		iguana_data_keys.append(row[0])

with open(VITRO_DATA_SRC, newline='') as vitroInput:
	for row in csv.reader(vitroInput):
		vitro_data.append(row)
		vitro_data_keys.append(row[0])

def formatTimezone(dt, local_tz):
	return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d/%m/%Y %H:%M:%S')

with open(RESULTS_SRC, 'w', newline='') as csvfile:
	results = csv.writer(csvfile, delimiter=',')
	for vcode in vitro_data_keys:
		if vcode in iguana_data_keys:
			#list of indexes
			IGindices = [i for i, x in enumerate(iguana_data_keys) if x == vcode]
			Vindices = [i for i, x in enumerate(vitro_data_keys) if x == vcode]

			for IGindex in IGindices:
				for Vindex in Vindices:
					itime = datetime.strptime(iguana_data[IGindex][2], '%d/%m/%Y %H:%M:%S')
					vtime_formatted = formatTimezone(vitro_data[Vindex][2], local_tz)
					vtime = datetime.strptime(vtime_formatted, '%d/%m/%Y %H:%M:%S')
					if (itime == vtime) or (itime > vtime and vtime < (itime + timedelta(seconds=1))):
						actID = vitro_data[Vindex][1]
						vitroDT = vitro_data[Vindex][2]
						results.writerow(iguana_data[IGindex] + [vtime] + [vitroDT] + [actID])
						#remove from search
						IGindices.remove(IGindex)
						Vindices.remove(Vindex)
					print(IGindices)
					print(Vindices)
					print(IGindex)
					print(Vindex)

			#remove from search
			for IGindex in IGindices:
				del iguana_data[IGindex]
				del iguana_data_keys[IGindex]

			for Vindex in Vindices:
				del vitro_data[Vindex]
				del vitro_data_keys[Vindex]
