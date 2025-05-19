import pytest
from weather import WeatherStation

def test_collect_data():
    ws = WeatherStation()
    data = ws.collect_data()
    assert "temperature" in data
    assert "humidity" in data
    assert "timestamp" in data
    assert "day" in data
    assert isinstance(data["temperature"], float)
    assert isinstance(data["humidity"], float)
    assert isinstance(data["timestamp"], str)
    assert isinstance(data["day"], str)

def test_get_data_by():
    ws = WeatherStation()
    for _ in range(5):
        ws.collect_data()
    day_data = ws.get_data_by()
    assert isinstance(day_data, dict)
    for day, temp in day_data.items():
        assert isinstance(day, str)
        assert isinstance(temp, float)

def test_average_temperature():
    ws = WeatherStation()
    ws.collect_data()
    avg = ws.average_temperature()
    assert isinstance(avg, float)
    assert 15.0 <= avg <= 35.0

def test_summary():
    ws = WeatherStation()
    for _ in range(5):
        ws.collect_data()
    summary = ws.summary()
    assert "temperatures_by_day" in summary
    assert "average_temperature" in summary
    assert isinstance(summary["temperatures_by_day"], dict)
    assert isinstance(summary["average_temperature"], float)
