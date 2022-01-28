from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    stations_level_over_threshold_list = stations_level_over_threshold(stations, 0.8)
    #Check that relative levels are over threshold
    for i in stations_level_over_threshold_list:
        assert i[1]>=0.8
    #Check that list is corectly sorted
    assert sorted(stations_level_over_threshold_list, key=lambda x: x[1], reverse=True)==stations_level_over_threshold_list

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    stations_highest_rel_level_list = stations_highest_rel_level(stations, 10)
    #Check that the list is correct length
    assert len(stations_highest_rel_level_list) == 10
    #Check that it is correctly sorted
    assert sorted(stations_highest_rel_level_list, key=lambda x: x[1], reverse=True)==stations_highest_rel_level_list