# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import sqrt

def station_by_distance(stations, p):
	output_list = []
	for station in stations:
		distance = sqrt((station.coord[0]-p[0])**2+(station.coord[1]-p[1])**2)
		output_list.append((station,distance))
	return sorted(output_list, key=lambda x: x[1])