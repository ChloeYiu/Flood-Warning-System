# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import sqrt, asin, sin, cos, pi

def great_circle_distance(coord1, coord2):
	lat1, lon1 = coord1
	lat2, lon2 = coord2
	lat1 = lat1/180*pi
	lon1 = lon1/180*pi
	lat2 = lat2/180*pi
	lon2 = lon2/180*pi
	return 6371*2*asin(sqrt((sin((lat1-lat2)/2))**2+cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))

def station_by_distance(stations, p):
	output_list = []
	for station in stations:
		distance = great_circle_distance(station.coord, p)
		output_list.append((station,distance))
	return sorted(output_list, key=lambda x: x[1])

def stations_within_radius(stations, centre, r):
	output_list = []
	for station in stations:
		distance = great_circle_distance(station.coord, centre)
		if distance<r:
			output_list.append(station)
	return output_list