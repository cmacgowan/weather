#
# System: Test System V-36
# Lambda: lambda_function.lambda_handler
# Author: Chris Macgowan 
# Date: 09 Sep 2019
#
# Description: 
#
# We are working from a series of tutorials. We are attempting to learn more about the AWS 
# lambda functions and all we can do with them. 
# 
# We will attempt to implement the following in some fashion: 
# - Upload data to a s3 bucket 
# - Ingest that data using a trigger on the s3 bucket 
# - Process the data in some way 
# - Write data to a data source 
# - Write data to a data lake (really
#
# We are thinking about making this AWS Lamda component the controller
# it will do all the following stuff:
#
# - s3 Bucket (build on the AWS Dashboad)
# - s3-trigger (The controller)
# - s3-trigger-process-a (process the temperature)
# - s3-trigger-process-b (process the humidity)
# - s3-trigger-storage (write data to the dynomoDB)
#
# When the file is dropped in to the s3 bucked this function will be called.
#

import json

import boto3


import controller as controllerModule


# from app import controller as controllerClass

# We are adding this here for testing
# We will move this to it's own lambda

#USERS_TABLE = os.environ['USERS_TABLE']
USERS_TABLE = 'weather-process-data'
client = boto3.client('dynamodb')



# test class
class LambdaBase():
    x = 5

    def __init__(self, x):
        self.x = x

    @classmethod
    def get_test_data(cls):
        return 12


def lambda_handler(event, context):
    # TODO implement

    # We will leave this here for the moment
    print("Inside: lambda_function.lambda_handler - The trigger event is being handled. Have a nice day!")

    print("We are testing the LambdaBase class implementation")
    print("Create the lambdaBase object")
    print("Chris Macgowan")

    # create the object
    lambdaBase = LambdaBase(22)
    print("Debug: lambdaBase.x", lambdaBase.x)

    print("We are testing the BlueController class implementation")
    print("Create the BlueController object")

    # controller_object = controllerClass.BlueController(23)

    blue_controller = controllerModule.BlueController(23)
    # controller_object = BlueController(23)
    print("Debug: blue_controller.tint", blue_controller.tint)


    # define the s3 object
    s3 = boto3.client("s3")

    filename = ""

    # This will handle the events
    if event:

        print("Debug: ****** ACHTUNG *******")
        print("Debug: S3 Event is being handled")

        # We will log the event type
        print("Event: ", event)

        # Define the file object
        # The event is a dictionary. We will access Records to get the filename
        fileObj = event["Records"][0]

        # Now get the filename from the file object. Again the filename is stored in the
        # dictionary using the keys below
        filename = str(fileObj['s3']['object']['key'])
        print("Filename: ", filename)

        # We have the filename. We will now get the data in the file as an object
        # boto3 will be used to access the s3 file contents


        # We will pass in the s3 bucket name and then filename to get the data object.
        fileDataObj = s3.get_object(Bucket="aws-lambda-trigger-macgowan", Key=filename)
        print("File Data Object: ", fileDataObj)

        # Using the fileDataObj we can get the content in the data object
        fileContentObj = fileDataObj["Body"].read().decode('utf-8')
        print("File Content: ", fileContentObj)

        # We will try to get the Josn from the time

        json_object = json.loads(fileContentObj)

        process_data_id = json_object['WeatherBase']['UUID']
        produce_id = json_object['WeatherBase']['ProduceId']

        title = json_object['WeatherBase']['Title']
        description = json_object['WeatherBase']['Description']
        state_code = json_object['WeatherBase']['StateCode']
        state_id = json_object['WeatherBase']['StateId']
        temperature = json_object['WeatherBase']['Temperature']
        humidity = json_object['WeatherBase']['Humidity']
        variable_a = json_object['WeatherBase']['VariableA']
        variable_b = json_object['WeatherBase']['VariableB']
        variable_c = json_object['WeatherBase']['VariableC']
        date = json_object['WeatherBase']['Date']

        print("Debug: Weather Base Data: Title: ", title)
        print("Debug: Weather Base Data: process_data_id: ", process_data_id)
        print("Debug: Weather Base Data: date: ", date)

        # Now that we have the data from the file.
        # We will call the process lambda

        # This is a test payload. We will want to send our file contect
        payload = {"message": "Hi, you have been invoked"}

        # Now call the destination function using the invokeLambda object
        #response1 = invokeLambda.invoke(FunctionName="s3-trigger-process-a",
        #                               InvocationType="Event",
        #                               Payload=json.dumps(payload))

        # print("Debug: response1 (json): ", response1)

        print("Debug: ****** ACHTUNG *******")
        print("Debug: Invoke: aws-sam-s3-trigger-process-a-HelloWorldFunction-1O4Z4AUA0OV0S")

        # Create the invocation object
        invoke_lambda = boto3.client("lambda", region_name="us-east-1")

        # Now call the destination function using the invokeLambda object
        invoke_response = invoke_lambda.invoke(FunctionName="aws-sam-s3-trigger-process-a-HelloWorldFunction-1O4Z4AUA0OV0S",
                                              InvocationType="RequestResponse",
                                              Payload=json.dumps(json_object))

         # This is working :-)
        response_payload = json.loads(invoke_response['Payload'].read().decode("utf-8"))
        print("response_payload: {}".format(response_payload))

        # get the message from the body
        status_code = response_payload['statusCode']
        print("Debug: message: ", status_code)

        # Status code
        status_code = response_payload['statusCode']
        print("Debug: status_code: ", status_code)

        # get the message from the body
        body = response_payload['body']
        print("Debug: body: ", body)
        body_json_object = json.loads(body)
        message = body_json_object['message']
        print("Debug: message: ", message)

        data = response_payload['data']
        print("Debug: event: ", data)
        data_json_object = json.loads(data)
        variable_a = data_json_object['WeatherBase']['VariableA']
        print("Debug: variable_a: ", variable_a)

        print("Debug: ****** ACHTUNG *******")
        print("Debug: Invoke: s3-trigger-process-b-HelloWorldFunction-ZDBFJ9HEAJUY")

        # Create the invocation object
        invoke_lambda_2 = boto3.client("lambda", region_name="us-east-1")

        # Now call the destination function using the invokeLambda object
        invoke_response2 = invoke_lambda_2.invoke(FunctionName="s3-trigger-process-b-HelloWorldFunction-ZDBFJ9HEAJUY",
                                                  InvocationType="RequestResponse",
                                                  Payload=json.dumps(data_json_object))

        # This is working :-)
        response2_payload = json.loads(invoke_response2['Payload'].read().decode("utf-8"))
        print("response2_payload: {}".format(response2_payload))

        # get the message from the body
        status_code = response2_payload['statusCode']
        print("Debug: status_code: ", status_code)

        # Status code
        status_code = response2_payload['statusCode']
        print("Debug: status_code: ", status_code)

        # get the message from the body
        body = response2_payload['body']
        print("Debug: body: ", body)
        body_json_object = json.loads(body)
        message = body_json_object['message']
        print("Debug: message: ", message)

        data = response2_payload['data']
        print("Debug: event: ", data)
        data_json_object = json.loads(data)
        variable_b = data_json_object['WeatherBase']['VariableB']
        print("Debug: variable_b: ", variable_b)

        # Finally we will write the weather data to the dynomoDB store
        # this will be move into it's own lambda function

        # This is what the data is looking like :::

        # {
        #     "WeatherBase":
        #         {
        #             "UUID": "a8098c1a-f86e-11da-bd1a-00112444be1e",
        #             "ProduceId": "1432",
        #             "Title": "Base Weather Data",
        #             "Description": "This is the famous Base Weather Data",
        #             "StateCode": "MN",
        #             "StateId": "44",
        #             "Temperature": "56",
        #             "Humidity": "20",
        #             "VariableA": "1234",
        #             "VariableB": "7890",
        #             "VariableC": "Hello Joe",
        #             "Date": "20-Jun-2019:12:00:34"
        #         }
        # }

        print("Debug: ****** ACHTUNG *******")
        print("Debug: Prepare to load the data to dynomoDB")

        # Prepare to load the data
        print("Debug: Prepare to load the data to dynomoDB")
        print("Debug: Set variables from data_json_object")
        process_data_id = data_json_object['WeatherBase']['UUID']
        produce_id = data_json_object['WeatherBase']['ProduceId']

        title = data_json_object['WeatherBase']['Title']
        description = data_json_object['WeatherBase']['Description']
        state_code = data_json_object['WeatherBase']['StateCode']
        state_id = data_json_object['WeatherBase']['StateId']
        temperature = data_json_object['WeatherBase']['Temperature']
        humidity = data_json_object['WeatherBase']['Humidity']
        variable_a = data_json_object['WeatherBase']['VariableA']
        variable_b = data_json_object['WeatherBase']['VariableB']
        variable_c = data_json_object['WeatherBase']['VariableC']
        date = data_json_object['WeatherBase']['Date']

        print("Debug: Weather Base Data: Title: ", title)
        print("Debug: Weather Base Data: process_data_id: ", process_data_id)
        print("Debug: Weather Base Data: date: ", date)

        print("Debug: Write to dynomoDB")

        if not process_data_id:
             return jsonify({'error': 'Please provide process_data_id'}), 400

        resp = client.put_item(
             TableName=USERS_TABLE,
             Item={
                 'processDataId': {'S': process_data_id},
                 'ProduceId': {'S': produce_id},
                 'Title': {'S': title},
                 'Description': {'S': description},
                 'StateCode': {'S': state_code},
                 'StateId': {'S': state_id},
                 'Temperature': {'S': temperature},
                 'Humidity': {'S': humidity},
                 'VariableA': {'S': variable_a},
                 'VariableB': {'S': variable_b},
                 'VariableC': {'S': variable_c},
                 'Date': {'S': date}
             }
         )

        print("Debug: Write to dynomoDB was successful")


    return {
        'statusCode': 200,
        'body123': json.dumps("Hello from Lambda!"),
        'body': json.dumps({"message": "Hello from Lambda!", "filename": filename})
    }
