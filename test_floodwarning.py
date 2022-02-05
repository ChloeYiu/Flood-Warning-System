from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.floodwarning import floodwarning

def test_floodwarning():
    # Create a 'list' of station with just one station
    stations = build_station_list()
    update_water_levels(stations)
    stations = [stations[0]]
    
    # Call function
    severe_list, high_list, moderate_list, low_list = floodwarning(stations)

    # Assertion
    assert type(severe_list) == type([])
    assert type(high_list) == type([])
    assert type(moderate_list) == type([])
    assert type(low_list) == type([])

    