
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

def test_rivers_by_station_number():
    stations = build_station_list()
    N = 9
    river_dict = stations_by_river(stations)
    
    #check river_dict is a dictionary
    assert type(river_dict) == type(dict())

    river_list = []
    
    for river_name, station_obj_list in river_dict.items():
        river_tuple = (river_name, len(station_obj_list))
       
        #check river_tuple is a tuple
        assert type(river_tuple) == type(tuple())
        #check river_tuple is of length 2
        assert len(river_tuple) == 2

        river_list.append(river_tuple)

    greatest_list = sorted(river_list, key = lambda x: x[1], reverse=True)

    #check greatest_list contains all needed items
    assert len(greatest_list) == len(river_dict)
    #check greatest_list is sorted
    assert greatest_list[0][1] > greatest_list[-1][1]

    greatest_N_list = greatest_list[:N]

    #check greatest_N_list length = N
    assert len(greatest_N_list) == N

    for i in range(N):
        greatest_list.pop(0)

    #check greatest_list length = original length - N
    assert len(greatest_list) == len(river_dict) - N
    #check content in greatest_list & greatest_N_list is a tuple
    assert type(greatest_list[0]) == type(tuple())
    assert type(greatest_N_list[-1]) == type(tuple())
    #check content in tuples are integers
    assert type(greatest_list[0][1]) == type(int())
    assert type(greatest_N_list[-1][1]) == type(int())

    while True:
        if greatest_list[0][1] == greatest_N_list[-1][1]:
            greatest_N_list.append(greatest_list[0])
            greatest_list.pop(0)
        else:
            break
    return greatest_N_list