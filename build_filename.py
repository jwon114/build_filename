import csv, os
from datetime import datetime, timedelta
import pytz

#IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
#VITRO_DATA_SRC = 'C:\\Python\Data\\vitro_data.csv'
#RESULTS_SRC = 'D:\\Python\\build_filename\\data\\results.csv'
IGUANA_DATA_SRC = 'C:\\Python\\Data\\iguana_data.csv'
VITRO_DATA_SRC = 'C:\\Python\\Data\\vitro_data.csv'
RESULTS_SRC = 'C:\\Python\\Data\\results.csv'
NO_MATCH_SRC = 'C:\\Python\\Data\\no_match.csv'
FC_SRC = 'C:\\Python\\Data\\file_copy.csv'

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

with open(RESULTS_SRC, 'w', 1, newline='') as csvfile:	
	print('Opening file for writing')
	results = csv.writer(csvfile, delimiter=',')
	print('Calculating...')
	results.writerow(['MRN_EPISODE_NUMBER, GUID, IG_DATETIME, V_DATETIME_FORMATTED, V_DATETIME_UTC, ACT_ID'])
	iguana_total = len(iguana_data_keys)
	vitro_in_iguana = 0
	failed = 0
	
	invalid_vitro_data_keys = [key for key in vitro_data_keys if key not in iguana_data_keys]
	for key in invalid_vitro_data_keys:
		with open(NO_MATCH_SRC, 'a', 1) as no_match:
			no_match.write('No Vitro MRN_EPISODE_NUMBER in Iguana logs: ' + str(key) + '\n')
	
	for vcode in vitro_data_keys:
		if vcode in iguana_data_keys:			
			#list of indexes
			IGindices = [i for i, x in enumerate(iguana_data_keys) if x == vcode]
			Vindices = [i for i, x in enumerate(vitro_data_keys) if x == vcode]

			for IGindex in IGindices:
				match = False
				for Vindex in Vindices:
					itime = datetime.strptime(iguana_data[IGindex][2], '%d/%m/%Y %H:%M:%S')
					vtime_formatted = formatTimezone(vitro_data[Vindex][2], local_tz)
					vtime = datetime.strptime(vtime_formatted, '%d/%m/%Y %H:%M:%S')
					max_time = itime + timedelta(seconds=1)
					min_time = itime + timedelta(seconds=-1)
					if (itime == vtime) or (itime > vtime and vtime <= max_time) or (vtime >= min_time and vtime <= max_time):
						actID = vitro_data[Vindex][1]
						vitroDT = vitro_data[Vindex][2]
						results.writerow(iguana_data[IGindex] + [vtime_formatted] + [vitroDT] + [actID])
						with open(FC_SRC, 'a', 1, newline='') as fc_csvfile:
							fc_results = csv.writer(fc_csvfile, delimiter=',')
							fc_results.writerow([actID] + [iguana_data[IGindex][1]])
						match = True						
						break
					
				if match:
					Vindices.remove(Vindex)
					vitro_in_iguana += 1
				else:
					with open(NO_MATCH_SRC, 'a', 1) as no_match:
						print('No Datetime Match for Vitro Index :' + str(vitro_data[Vindex]))
						no_match.write('No Datetime Match for Vitro Index :' + str(vitro_data[Vindex]) + '\n')
						failed += 1
					
			#remove from search
			iguana_data = [data for data in iguana_data if iguana_data.index(data) not in IGindices]
			iguana_data_keys = [data for data in iguana_data_keys if iguana_data_keys.index(data) not in IGindices]		
				
	print('Finished processing: ' + str(vitro_in_iguana) + ' matching out of ' + str(iguana_total) + ' Iguana keys and ' + str(len(vitro_data_keys)) + ' Vitro keys, ' + str(failed) + ' failed with no datetime match')
	