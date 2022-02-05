# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.analysis import *
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib
import numpy as np

def test_polyfit():
    """Requirements for Task 2F"""
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0] #randomly pick a station to plot
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
    poly, d0 = polyfit(dates, levels, 4)

    #Test poly type
    assert type(poly) == type(np.poly1d([1]))

    #Test d0
    assert d0 == matplotlib.dates.date2num(dates)[0]