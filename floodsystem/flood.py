def stations_level_over_threshold(stations, tol):
	'''
	Takes a list of station objects and a tolerance level.  Returns a list of station objects with relative water level above tolerance.
	'''
	output_list = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None and station.relative_water_level()>tol]
	return sorted(output_list, key=lambda x: x[1], reverse=True)


def stations_highest_rel_level(stations, N):
	'''
	Takes a list of station objects and integer N.  Returns a list of the N stations (objects) with highest relative water level, sorted in ascending order
	'''
	output_list = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None]
	return sorted(output_list, key=lambda x: x[1], reverse=True)[:N]