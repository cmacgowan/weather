
# test_handler.py
# Hello Joe

import pytest

from app import humidity as humidityClass

## Test Setup Functions

def test_humidity():

    # create the controleller object

    humidity_object = humidityClass.Humidity(90)
    assert humidity_object.humidity == 90

    temp = humidity_object.get_humidity_by_state_id(41)
    assert temp == "60"





