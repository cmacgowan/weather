
# test_handler.py
# Hello Joe

import json
import boto3
import pytest
from app import app

## Test Setup Functions

import json
import os

# import jsonschema
import pytest

from app import app


TRIGGER_EVENT_FILE = os.path.join(
    os.path.dirname(__file__),
    'events',
    'aws_s3_event_publisher.json'
)

TRIGGER_EVENT_SCHEMA_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'events',
    'aws_s3_event_publisher_schema.json'
)

@pytest.fixture()
def trigger_event(trigger_event_file=TRIGGER_EVENT_FILE):
    # Trigger event
    with open(trigger_event_file) as f:
        return json.load(f)

@pytest.fixture()
def trigger_event_message(trigger_event):
    # Slack message
    # return h._get_message_from_event(trigger_event)
    return trigger_event

@pytest.fixture()
def trigger_event_message_schema():
    # trigger event message schema
    with open(TRIGGER_EVENT_SCHEMA_FILE_PATH) as f:
        return json.load(f)


def test_validate_test_class(trigger_event, trigger_event_message_schema):

    # Throws an exception on bad in put.
    # h._validate_slack_message_schema(slack_message, slack_message_schema)

    ret = app.lambda_handler("", "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "Hello from Lambda!"
    assert data["lambdaBase.x"] == 22


