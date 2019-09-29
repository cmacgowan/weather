#
# System: The Weather Process System
# Lambda: s3-trigger-process-b :: lambda_function.lambda_handler
# Process Humidity Data
# Author: Chris Macgowan
# Date: 09 Sep 2019
#
# Description:
#
# We are working from a series of tutorials. We are attempting to learn more about the AWS
# lambda functions and all we can do with them.
#
# This function will return a Humidity given a code.
#


import json

import humidity as humidityModule

# import requests


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

    print("Debug: Inside: s3-trigger-process-b-HelloWorldFunction-ZDBFJ9HEAJUY")
    print("Debug: We are about to update the JSON object - below are the pre-view")
    print("Debug: Event (json): ", event)

    print("Chris Macgowan")

    print("We are testing the Humidity class implementation")
    print("Create the Humidity object")

    humidity_obj = humidityModule.Humidity(88)
    print("Debug: tempObj.temp: ", humidity_obj.humidity)
    print("Debug: get_humidity_by_state_id(41): ", humidity_obj.get_humidity_by_state_id(41))
    print("Debug: get_humidity_by_state_id(44): ", humidity_obj.get_humidity_by_state_id(44))
    print("Debug: get_humidity_by_state_id(49): ", humidity_obj.get_humidity_by_state_id(49))
    print("Debug: get_humidity_by_state_id(99): ", humidity_obj.get_humidity_by_state_id(99))

    # get the humidity based on the state ID
    print("Debug: Update the JSON object - setting humidity using humidity_obj")
    print("Debug: Pre conditions")
    print("Debug: StateId: ", event['WeatherBase']['StateId'])
    print("Debug: Humidity: ", event['WeatherBase']['Humidity'])
    print("Debug: Get the humidity based on StateId")
    humidity_for_state = humidity_obj.get_humidity_by_state_id(int(event['WeatherBase']['StateId']))
    print("Debug: humidity_for_state: ", humidity_for_state)

    print("Debug: Set humidity back to the JSON object")
    event['WeatherBase']['Humidity'] = humidity_for_state
    print("Debug: Humidity: ", event['WeatherBase']['Humidity'])

    # Just a test
    event['WeatherBase']['VariableB'] = "Updated by: s3-trigger-process-b-HelloWorldFunction-ZDBFJ9HEAJUY"

    print("Debug: Inside: s3-trigger-process-b-HelloWorldFunction-ZDBFJ9HEAJUY")
    print("Debug: We are about the print the Event")
    print("Debug: Event (json): ", event)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Lambda - s3-trigger-process-b"}),
        "data": json.dumps(event)
    }
