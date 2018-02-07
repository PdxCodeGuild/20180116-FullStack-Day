import datetime


# LOAD FILE (V1)
def load_file(filename):
	with open('sunnyside.rain.txt', 'r') as rain_file:  # OPEN/ READ FILE
		rain_data = rain_file.read().lower().split('\n')  # LOWER CASE & SPLIT BY LINE
		rain_data_points = {}  # EMPTY DICTIONARY FOR DATA POINTS
		for line in rain_data:
			try:  # TRY EXCEPT TO ISOLATE DATA POINTS FROM OTHER TXT IN FILE
				date = datetime.datetime.strptime(line.split()[0], '%d-%b-%Y')
				# date = date.strftime('%d-%b-%Y')
				total_rain = float(line.split()[1])
				rain_data_points[date] = total_rain
			except ValueError:
				pass
			except IndexError:
				pass
		return rain_data_points


load_file('sunnyside.rain.txt')


# VERSION 2: AVG & VAR
# AVERAGE
def mean_data(rain_data_points: dict):
	sum_running = 0
	data_pairs = rain_data_points.items()
	for key, value in data_pairs:
		sum_running += value
	avg = sum_running / (len(data_pairs))
	return avg


print(str('\nthe average rainfall for this region is: ' + str(mean_data(rain_data_points=load_file('sunnyside.rain.txt')))))


# VARIANCE
def var_data(rain_data_points: dict):
	sum_running_2 = 0
	data_pairs_2 = rain_data_points.items()
	avg = mean_data(rain_data_points)
	for key, value in data_pairs_2:
		square = ((value - avg) ** 2)
		sum_running_2 += square
	variance = sum_running_2 / (len(data_pairs_2) - 1)
	return variance


print(str('\nthe rainfall variance for this region is: ' + str(var_data(rain_data_points=load_file('sunnyside.rain.txt')))))


# RAINIEST DAY
def rainiest_day(rain_data_points: dict):
	data_pairs_3 = rain_data_points.items()
	rainiest_day_ = {'max_rain': 0, 'rainiest_day': []}
	for key, value in data_pairs_3:
		if value > rainiest_day_['max_rain']:
			rainiest_day_['max_rain'] = value
	for key, value in data_pairs_3:
		if value == rainiest_day_['max_rain']:
			rainiest_day_['rainiest_day'].append(key)
	return print('\nthe rainiest day in this region was: ' + str(rainiest_day_['rainiest_day']) + '\nwith ' + str(rainiest_day_['max_rain']) + ' units of rain.')


rainiest_day(rain_data_points=load_file('sunnyside.rain.txt'))


# RAINIEST YEAR
def rainiest_year(rain_data_points: dict):
	years = list(set([data.year for data in rain_data_points.keys()]))
	data_by_year = {year: {'rain_data': [value for key, value in rain_data_points.items() if key.year == year]} for year in years}
	for year in data_by_year.keys():
		data_by_year[year]['avg_rain'] = sum(data_by_year[year]['rain_data']) / len(data_by_year[year]['rain_data'])
		rainiest_year_ = {'max_avg_daily_rain': 0, 'rainiest_year': []}
	for year in data_by_year.keys():
		if data_by_year[year]['avg_rain'] > rainiest_year_['max_avg_daily_rain']:
			rainiest_year_['max_avg_daily_rain'] = data_by_year[year]['avg_rain']
	for year in data_by_year.keys():
		if data_by_year[year]['avg_rain'] == rainiest_year_['max_avg_daily_rain']:
			rainiest_year_['rainiest_year'].append(year)
	return print('\nthe rainiest year in this region was: ' + str(rainiest_year_['rainiest_year']) + ' with ' + str(rainiest_year_['max_avg_daily_rain']) + ' units of rain on average.')


rainiest_year(rain_data_points=load_file('sunnyside.rain.txt'))
