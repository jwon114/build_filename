
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

#['27/12/2016 14:51', '09/01/2017 15:36', '09/01/2017 19:44', '09/01/2017 19:46', '09/01/2017 19:46']
local_tz = pytz.timezone('Australia/Sydney')

#testing
local_dt = datetime.strptime('2016-12-27 03:51:48.313', '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz)
#print(local_dt)


for vtime in vitro_time:
  index = vitro_time.index(vtime)
  vitro_time_formatted = datetime.strptime(vtime, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d/%m/%Y %H:%M:%S')
  vitro_time[index] = vitro_time_formatted

print(vitro_time)

for itime in iguana_time:
  for vtime in vitro_time:
    itime_formatted = datetime.strptime(itime, '%d/%m/%Y %H:%M:%S')
    max_time = itime_formatted + timedelta(minutes=5)
    vtime_formatted = datetime.strptime(vtime, '%d/%m/%Y %H:%M:%S')
    if itime_formatted > vtime_formatted and vtime_formatted < max_time:
      print(itime)

#print(vitro_time)
