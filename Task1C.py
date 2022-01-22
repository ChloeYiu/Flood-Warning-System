# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    alphabetically_sorted = sorted(stations_within_radius_list, key=lambda x: x.name)
    print([i.name for i in alphabetically_sorted])

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
