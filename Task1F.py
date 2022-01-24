# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import *

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_stations_name = [i.name for i in inconsistent_stations]
    inconsistent_stations_name.sort()
    print(inconsistent_stations_name)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()