# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)

    trange_r1 = (1, 2)
    trange_r2 = (-1, 0)
    trange_w1 = (2, 1)
    trange_w2 = (0.2, -1.23)
    trange_w3 = None

    river = "River X"
    town = "My Town"

    r1 = MonitoringStation(s_id, m_id, label, coord, trange_r1, river, town)
    r2 = MonitoringStation(s_id, m_id, label, coord, trange_r2, river, town)
    w1 = MonitoringStation(s_id, m_id, label, coord, trange_w1, river, town)
    w2 = MonitoringStation(s_id, m_id, label, coord, trange_w2, river, town)
    w3 = MonitoringStation(s_id, m_id, label, coord, trange_w3, river, town)

    assert r1.typical_range_consistent() == True
    assert r2.typical_range_consistent() == True
    assert w1.typical_range_consistent() == False
    assert w2.typical_range_consistent() == False
    assert w3.typical_range_consistent() == False

def test_inconsistent_typical_range_stations():
    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)

    trange_r1 = (1, 2)
    trange_r2 = (-1, 0)
    trange_w1 = (2, 1)
    trange_w2 = (0.2, -1.23)
    trange_w3 = None

    river = "River X"
    town = "My Town"

    r1 = MonitoringStation(s_id, m_id, label, coord, trange_r1, river, town)
    r2 = MonitoringStation(s_id, m_id, label, coord, trange_r2, river, town)
    w1 = MonitoringStation(s_id, m_id, label, coord, trange_w1, river, town)
    w2 = MonitoringStation(s_id, m_id, label, coord, trange_w2, river, town)
    w3 = MonitoringStation(s_id, m_id, label, coord, trange_w3, river, town)
    
    stations = [r1, r2, w1, w2, w3]

    assert inconsistent_typical_range_stations(stations) == [w1, w2, w3]