
import datetime
from floodsystem.datafetcher import fetch_measure_levels

def floodwarning(stations):
    '''Takes in a list of station objects
        Returns four list of tuples (MonitoringStation object, risk factor) categorized according to severity of flood risk
        '''

    # Fetch a list of stations with their relative water level 
    stations_with_level = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None]
    
    # Arrange the list of stations from highest to lowest relative water level
    stations_with_level_sorted = sorted(stations_with_level, key=lambda x: x[1], reverse=True)

    # Calculate risk factor
    # Risk factor is based on
        # The latest water level
        # THe trend of water level change in the previous 1h with weighted average
    stations_with_risk_factor = []
    for station_tuple in stations_with_level_sorted:
        try:
            station = station_tuple[0]
            latest_level = station_tuple[1]
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))
            relative_level_diff_15 = (levels[0] - levels[1])/(station.typical_range[1]-station.typical_range[0])
            relative_level_diff_30 = (levels[0] - levels[2])/(station.typical_range[1]-station.typical_range[0])
            relative_level_diff_45 = (levels[0] - levels[3])/(station.typical_range[1]-station.typical_range[0])
            relative_level_diff_60 = (levels[0] - levels[4])/(station.typical_range[1]-station.typical_range[0])
            risk_factor = latest_level + relative_level_diff_15*0.2 + relative_level_diff_30*0.15 + relative_level_diff_45*0.1 + relative_level_diff_60*0.05
            stations_with_risk_factor.append((station, risk_factor))
        except:
            pass
    stations_with_risk_factor_sorted = sorted(stations_with_risk_factor, key=lambda x: x[1], reverse=True)

    # Categorize data
    severe_list = [station_tuple for station_tuple in stations_with_risk_factor_sorted if station_tuple[1] >= 1.2]
    high_list = [station_tuple for station_tuple in stations_with_risk_factor_sorted if station_tuple[1] >= 0.8 and station_tuple[1] < 1.2]
    moderate_list = [station_tuple for station_tuple in stations_with_risk_factor_sorted if station_tuple[1] >= 0.5 and station_tuple[1] < 0.8]
    low_list = [station_tuple for station_tuple in stations_with_risk_factor_sorted if station_tuple[1] < 0.5]

    return severe_list, high_list, moderate_list, low_list



    
        
        