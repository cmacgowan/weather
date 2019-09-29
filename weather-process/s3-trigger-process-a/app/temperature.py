#
# System: The Weather Process System
# Lambda: s3-trigger-process-a :: lambda_function.lambda_handler
# Class: Temperature
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
# Switch Map
# https://jaxenter.com/implement-switch-case-statement-python-138315.html
#


import json

import boto3

# test class
class Temperature():

    temp = 5

    def __init__(self, temp):
        self.temp = temp

    @classmethod
    def get_temperature_by_state_id(cls, state_id):

        temp_map = {
            41: "23",
            42: "45",
            43: "2",
            44: "38",
            45: "20",
            46: "78",
            47: "108",
            48: "109",
            49: "888"
        }

        return temp_map.get(state_id, "NA")

