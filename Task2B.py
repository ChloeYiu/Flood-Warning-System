# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""
    stations = build_station_list()
    update_water_levels(stations)
    stations_level_over_threshold_list = stations_level_over_threshold(stations, 0.8)
    for i in stations_level_over_threshold_list:
    	print(i[0].name+" "+str(i[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()