# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    #Example Code
    station_by_distance_list = station_by_distance(stations, (52.2053,0.1218))
    nearest_10=[]
    print("Nearest")
    for i in station_by_distance_list[:10]:
        nearest_10.append((i[0].name, i[1]))
    print(nearest_10)
    
    print("Furthest")
    furthest_10=[]
    for i in station_by_distance_list[-10:]:
        furthest_10.append((i[0].name, i[1]))
    print(furthest_10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
