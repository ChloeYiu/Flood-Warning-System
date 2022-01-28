# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""
    stations = build_station_list()
    update_water_levels(stations)
    stations_highest_rel_level_list = stations_highest_rel_level(stations, 10)
    for i in stations_highest_rel_level_list:
    	print(i[0].name+" "+str(i[1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()