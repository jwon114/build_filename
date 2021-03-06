
from datetime import datetime, timedelta
import pytz

iguana_time = ['27/12/2016 14:51:50',
'09/01/2017 15:36:24',
'09/01/2017 19:44:56',
'09/01/2017 19:46:34',
'09/01/2017 19:46:36']


vitro_time = ['2016-12-27 03:51:48.313',
'2017-01-09 04:36:22.447',
'2017-01-09 08:44:56.597',
'2017-01-09 08:46:34.493',
'2017-01-09 08:46:36.557']

# Vitro to local time
#['27/12/2016 14:51:48', '09/01/2017 15:36:22', '09/01/2017 19:44:56', '09/01/2017 19:46:34', '09/01/2017 19:46:36']
local_tz = pytz.timezone('Australia/Sydney')

#testing
local_dt = datetime.strptime('2016-12-27 03:51:48.313', '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz)
#print(local_dt)


for vtime in vitro_time:
  index = vitro_time.index(vtime)
  vitro_time_formatted = datetime.strptime(vtime, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d/%m/%Y %H:%M:%S')
  vitro_time[index] = vitro_time_formatted

#print(vitro_time)

vitro_time_formatted = datetime.strptime('2017-01-22 06:18:30.050', '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d/%m/%Y %H:%M:%S')

print(vitro_time_formatted)
igtime = datetime.strptime('22/01/2017 17:18:29', '%d/%m/%Y %H:%M:%S')
igtime = igtime + timedelta(seconds=1)
vitro_time_formatted = datetime.strptime(vitro_time_formatted, '%d/%m/%Y %H:%M:%S')

if vitro_time_formatted < igtime:
  print('yes')

for itime in iguana_time:
  for vtime in vitro_time:
    itime_formatted = datetime.strptime(itime, '%d/%m/%Y %H:%M:%S')
    max_time = itime_formatted + timedelta(seconds=3)
    vtime_formatted = datetime.strptime(vtime, '%d/%m/%Y %H:%M:%S')
    #if itime_formatted > vtime_formatted and vtime_formatted < max_time:
      #print(max_time)

#print(vitro_time)
