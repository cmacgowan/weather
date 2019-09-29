
# test_handler.py
# Hello Joe

import pytest

from app import temperature as temperatureClass

## Test Setup Functions

def test_temperature():

    # create the controleller object

    temperature_object = temperatureClass.Temperature(23)
    assert temperature_object.temp == 23

    temp = temperature_object.get_temperature_by_state_id(41)
    assert temp == "23"





