# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    rivers_with_station_list = rivers_with_station(stations)
    print(str(len(rivers_with_station_list))+" rivers with station(s). The first 10 are...")
    print(sorted(rivers_with_station_list)[:10])

    stations_by_river_list = stations_by_river(stations)
    aire_stations = [i.name for i in stations_by_river_list["River Aire"]]
    cam_stations = [i.name for i in stations_by_river_list["River Cam"]]
    thames_stations = [i.name for i in stations_by_river_list["River Thames"]]
    print("River Aire")
    print(sorted(aire_stations))
    print("River Cam")
    print(sorted(cam_stations))
    print("River Thames")
    print(sorted(thames_stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
