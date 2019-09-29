
# test_handler.py
# Hello Joe

import json
import boto3
import pytest
from app import app

## Test Setup Functions

def test_handler_moves_incoming_object_to_processed():

    # assert call(None, None) == None

    ret = app.lambda_handler("", "")
    data = json.loads(ret["body"])

    print("Debug: Data 123 object: data: ", data)

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "Hello from Lambda!"


    # assert "location" in data.dict_keys()

def test_handler_trigger():

    # assert call(None, None) == None

    ret = app.lambda_handler("", "")
    data = json.loads(ret["body"])

    print("Debug: Data 123 object: data: ", data)

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]


