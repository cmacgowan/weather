
# test_handler.py
# Hello Joe

import pytest

from app import controller as controllerClass

## Test Setup Functions

def test_controller():

    # create the controleller object

    controller_object = controllerClass.BlueController(23)

    assert controller_object.tint == 23



