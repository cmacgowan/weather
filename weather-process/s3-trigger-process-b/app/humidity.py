#
# System: The Weather Process System
# Lambda: s3-trigger-process-b :: lambda_function.lambda_handler
# Class: Humidity
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
# Switch Map
# https://jaxenter.com/implement-switch-case-statement-python-138315.html
#


import json

import boto3

# test class
class Humidity():

    humidity = 5

    def __init__(self, humidity):
        self.humidity = humidity

    @classmethod
    def get_humidity_by_state_id(cls, state_id):

        humidity_map = {
            41: "60",
            42: "50",
            43: "53",
            44: "90",
            45: "93",
            46: "40",
            47: "10",
            48: "11",
            49: "99"
        }

        return humidity_map.get(state_id, "NA")

