# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def run():
    """Requirements for Task 2F"""
    # Fetch the 5 stations with the highest current relative water level
    stations = build_station_list()
    update_water_levels(stations)
    stations_highest_5 = stations_highest_rel_level(stations, 5)
    print(stations_highest_5)

    for i in stations_highest_5:
        station = i[0]
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt)) 

        try:
            # Add typical range low/high on plot
            low_line = [station.typical_range[0]]*len(levels)
            high_line = [station.typical_range[1]]*len(levels)
            plt.plot(dates, low_line)
            plt.plot(dates, high_line)
            # Plot level data and the best-fit polynomial of degree 4 against time
            plot_water_level_with_fit(station, dates, levels, 4)
        
        except:
            pass
            # Note: the first largest datum is broken - it has no data for the previous 2 days


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()