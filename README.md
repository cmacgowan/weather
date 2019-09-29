# weather




Bluerayon Development Labs
The Weather Process Test 
The Even More Famous Technical Document
Copyright (c) 2005-2019 Bluerayon Development Labs
Chris Macgowan 
11 Sep 2019
weather_process.txt

Description: 

We are trying to build a system. This folder will contain all the parts. 

We will keep you posted. 

This is the technical documentation for the Weather Process System. Weather Process System is a collection of AWS components. The The Weather Process System is used for demonstration. 

Each component as it's own Technical Document :-) 

-----------------------------------------------------------------------------
Software License

MIT License

Copyright (c) 2005-2019 Bluerayon Development Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

MIT License
https://opensource.org/licenses/MIT


-----------------------------------------------------------------------------
Introduction

None


-----------------------------------------------------------------------------
Resources

Tutorial: Deploying a Hello World Application
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html


-----------------------------------------------------------------------------
Construction

A couple notes on the construction of this AWS Lambda. This s3-trigger was origianlly built in the AWS Dashboard. We wanted to build the Lambda so we could use the AWS SAM CLI to deploy the Lambda. We used the following process to do this. 

With the s3-trigger built and functional from the AWS Dashboard

- The AWS SAM CLI is installed and operational

- From the AWS Dashboard download, user the Actions and Export Function
- From the Export Menu choose Download AWS SAM File
- s3-trigger.yaml is downloaded

- Change to a working folder

- Execute $ sam init --runtime python3.7
- The template hello world app is created

- Change root folder from sam-app to s3-trigger 
- Change the app folder from hello_world to app
- Overwrite the template.yaml from the downloaded s3-trigger.yaml
- Update the CodeUri: from . to app/
- Update the app.py
- build was successful

Notes: 

- Follow the Package and Deploy proceedures below to deploy the Lambda component. 

- The new deployed lambda function will be creatd as aws-sam-s3-trigger-s3trigger-1PEHK9TO3RL0. So note that the old lambda s3-trigger remains. I can be deleted. 

- I think that we also manually had to add back the trigger on the sq bucket to the new lambda. bla bla bla bla ...

- When running from the Dashboard after the deploy we might of had to update the name of the function in the Dashboard. All was ok on the next deploy

****
HELLO 

We build some stuff on the AWS dashboard and want to create a SAM creap 
Crap - 

s3-trigger

Notes: 

Tutorial: Deploying a Hello World Application
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

We are going to start by using the template project above to create the project struture 

We attempted the following:
- sam init --runtime python3.7
- change the name and update the app.py
- build failed

Now we will try again ...
We read the readme.md and you have to change the CodeUri to get the path 
to the app folder (hello_world) in the demo 

We attempted the following:
- sam init --runtime python3.7
- Change root folder from sam-app to s3-trigger 
- Change the app folder from hello_world to app
- Overwrite the template.yaml from the downloaded s3-trigger.yaml
- Update the CodeUri: from . to app/
- Update the app.py
- build was successful


-----------------------------------------------------------------------------
The System

The Weather Process System was created to learn some stuff about AWS Lambda and provide a platfor for demonstation of testing principles.

The Weather Process System consisita of the following components. 

- s3 Bucket (build on the AWS Dashboad)
- s3-trigger (The controller)
- s3-trigger-process-a (process the temperature)
- s3-trigger-process-b (process the humidity)
- s3-trigger-storage (write data to the dynomoDB) 


-----------------------------------------------------------------------------
General Notes 

None


-----------------------------------------------------------------------------
Execution

The following commands can be used to build, package, deploy and run the app. 

* The Commands below have been updated to support s3-trigger
* --stack-name aws-sam-s3-trigger

// Build the application 
sam build

// Package the application for deployment
sam package --output-template packaged.yaml --s3-bucket aws-sam-bucket-macgowan

// Deploy the application to the AWS cloud
sam deploy --template-file packaged.yaml --region us-east-1 --capabilities CAPABILITY_IAM --stack-name aws-sam-s3-trigger

* Can't really test it as it dies not expose an API - we should add one :

// Test the application in the AWS Cloud
aws cloudformation describe-stacks --stack-name aws-sam-s3-trigger --region us-east-1 --query "Stacks[].Outputs"

// Testing Your Application Locally (Optional)
sam local start-api 


END OF DOCUMENT 
HAVE A NICE DAY 
V-367.900













