#
# System: The Weather Process System
# Lambda: s3-trigger-process-a :: lambda_function.lambda_handler
# Process Temperature Data
# Author: Chris Macgowan
# Date: 09 Sep 2019
#
# Description:
#
# We are working from a series of tutorials. We are attempting to learn more about the AWS
# lambda functions and all we can do with them.
#
# This function will return a Temperture given a code.
#


import json

# import requests

import temperature as temperatureModule


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    print("Debug: Inside: aws-sam-s3-trigger-process-a-HelloWorldFunction-1O4Z4AUA0OV0S")
    print("Debug: We are about to update the JSON object - below are the pre-view")
    print("Debug: Event (json): ", event)

    print("Chris Macgowan")



    print("We are testing the Temperature class implementation")
    print("Create the Temperature object")

    temp_obj = temperatureModule.Temperature(23)
    print("Debug: tempObj.temp: ", temp_obj.temp)
    print("Debug: get_temperature_by_state_id(41): ", temp_obj.get_temperature_by_state_id(41))
    print("Debug: get_temperature_by_state_id(44): ", temp_obj.get_temperature_by_state_id(44))
    print("Debug: get_temperature_by_state_id(49): ", temp_obj.get_temperature_by_state_id(49))
    print("Debug: get_temperature_by_state_id(99): ", temp_obj.get_temperature_by_state_id(99))

    # get the temp based on the state ID
    print("Debug: Update the JSON object - setting temperature using temp_obj")
    print("Debug: Pre conditions")
    print("Debug: StateId: ", event['WeatherBase']['StateId'])
    print("Debug: Temperature: ", event['WeatherBase']['Temperature'])
    print("Debug: Get the temperature based on StateId")
    temperature_for_state = temp_obj.get_temperature_by_state_id(int(event['WeatherBase']['StateId']))
    print("Debug: temperature_for_state: ", temperature_for_state)

    print("Debug: Set temperature back to the JSON object")
    event['WeatherBase']['Temperature'] = temperature_for_state
    print("Debug: Temperature: ", event['WeatherBase']['Temperature'])

    # Just a test
    event['WeatherBase']['VariableA'] = "Updated by: aws-sam-s3-trigger-process-a-HelloWorldFunction-1O4Z4AUA0OV0S"


    # This is the business

    # The event will contain the code.
    # we will pass the code the Temerature Class (The busiess)
    # This will make the business easter to test

    print("Debug: Inside: aws-sam-s3-trigger-process-a-HelloWorldFunction-1O4Z4AUA0OV0S")
    print("Debug: We are about the print the Event")
    print("Debug: Event (json): ", event)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Lambda - s3-trigger-process-a"}),
        "data": json.dumps(event)
    }
