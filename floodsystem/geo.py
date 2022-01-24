# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import sqrt, asin, sin, cos, pi

def great_circle_distance(coord1, coord2):
	"""Takes in two tuples of lat/lon coords, and returns their great circle distance"""
	lat1, lon1 = coord1
	lat2, lon2 = coord2
	lat1 = lat1/180*pi
	lon1 = lon1/180*pi
	lat2 = lat2/180*pi
	lon2 = lon2/180*pi
	return 6371*2*asin(sqrt((sin((lat1-lat2)/2))**2+cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))

def station_by_distance(stations, p):
	"""Takes in a list of station objects, and a tuple of lat/lon coords
	Returns a sorted list of stations with their corresponding distance from coord"""
	output_list = []
	for station in stations:
		distance = great_circle_distance(station.coord, p)
		output_list.append((station,distance))
	return sorted(output_list, key=lambda x: x[1])

def stations_within_radius(stations, centre, r):
	"""Takes in a list of station objects, a tuple of lat/lon coords indicating the circle's centre, and a float indicating circle's radius
	Returns a list of stations within the circle/radius defined"""
	output_list = []
	for station in stations:
		distance = great_circle_distance(station.coord, centre)
		if distance<r:
			output_list.append(station)
	return output_list

def rivers_with_station(stations):
	"""Takes in a list of station objects, returns a list of rivers with at least one station"""
	output_set = set()
	for station in stations:
		output_set.add(station.river)
	return output_set

def stations_by_river(stations):
	"""Takes in a list of station objects, returns a dictionary of rivers (keys) matched to a list of their corresponding stations (values)"""
	output_dict = dict()
	for station in stations:
		if station.river in output_dict:
			output_dict[station.river].append(station)
		else:
			output_dict[station.river]=[station]
	return output_dict

def rivers_by_station_number(stations, N):

    """Takes in a list of stations object and an integer N
	
	Returns a list of tuples that shows the name of top N rivers 
	with the greatest number of monitoring stations, and their respective numbers

    The tuples are arranged from the ones with the most stations to the least stations

    """

    river_dict = stations_by_river(stations)
    river_list = [] 
    for river_name, station_obj_list in river_dict.items():
        river_tuple = (river_name, len(station_obj_list))
        river_list.append(river_tuple)
    greatest_list = sorted(river_list, key = lambda x: x[1], reverse=True)
    greatest_N_list = greatest_list[:N]
    for i in range(N):
        greatest_list.pop(0)
    while True:
        if greatest_list[0][1] == greatest_N_list[-1][1]:
            greatest_N_list.append(greatest_list[0])
            greatest_list.pop(0)
        else:
            break
    return greatest_N_list
