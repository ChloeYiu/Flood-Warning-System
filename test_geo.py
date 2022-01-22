
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def test_great_circle_distance():
    assert round(great_circle_distance((0.1,0.2),(0.5, 0.6)),1)==62.9

def test_station_by_distance():
    stations = build_station_list()
    station_by_distance_list = station_by_distance(stations, (52.2053,0.1218))
    #Check it's sorted
    assert sorted(station_by_distance_list, key=lambda x: x[1])==station_by_distance_list
    #Check distances are right
    for i in station_by_distance_list:
        assert i[1]==great_circle_distance(i[0].coord, (52.2053,0.1218))

def test_stations_within_radius():
    stations = build_station_list()
    stations_within_radius_list = stations_within_radius(stations, (52.2053,0.1218), 10)
    #Check all are within radius
    for i in stations_within_radius_list:
        assert great_circle_distance(i.coord, (52.2053,0.1218)) <= 10

def test_rivers_with_station():
    stations = build_station_list()
    rivers_with_station_list = rivers_with_station(stations)

def test_stations_by_river():
    stations = build_station_list()
    stations_by_river_dict = stations_by_river(stations)
    for i in stations_by_river_dict.keys():
        for j in stations_by_river_dict[i]:
            assert j.river == i