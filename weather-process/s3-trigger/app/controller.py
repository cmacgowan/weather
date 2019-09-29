#
# System: Test System V-36
# Lambda: lambda_function.lambda_handler
# Author: Chris Macgowan 
# Date: 09 Sep 2019
# Controller
#
# Description: 
#
# This is a little test class - maybe it will be the controller someday.
#

import json

import boto3

# test class
class BlueController():

    tint = 5

    def __init__(self, tint):
        self.tint = tint

    @classmethod
    def get_test_data(cls):
        return 12
