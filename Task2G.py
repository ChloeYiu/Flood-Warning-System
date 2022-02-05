# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.floodwarning import floodwarning
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2G"""
    # Create station list
    stations = build_station_list()
    update_water_levels(stations)

    # Reduce the number of stations in the list for demonstration convenience
    demo_stations_tuplelist = stations_highest_rel_level(stations, 10)
    demo_stations = [demo_stations_tuple[0] for demo_stations_tuple in demo_stations_tuplelist]
    
    # Generate categorized list
    severe_list, high_list, moderate_list, low_list = floodwarning(demo_stations)

    # Print output
    print('')
    print('Stations with severe flood risk: ')
    if len(severe_list) == 0:
        print('There is no place with severe flood risk')
        print('')
        print('Stations with high flood risk: ')
        for station_tuple in high_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.name)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())

    else: 
        for station_tuple in severe_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.name)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()