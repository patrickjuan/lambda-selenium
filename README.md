# Selenium minimal serverless service

This repository has a minimal service to run Selenium on AWS Lambda using Serverless Framework.

## What is Selenium

### The project
​​Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.
It can be used for automated testing but not just that, we can use it to automate basically everything that runs in a browser.


## Prerequisites

These instructions will get you a copy of the service up and running on your local machine for development and testing purposes.

Make sure you have all the following prerequisites:

### Serverless

This serverless is lambda function using serverless framework. Ensure, you have [node and npm](https://nodejs.org/en/download/) installed before you start.
```
$ npm install -g serverless@1.52.0
```

### Python

This service uses Python version 3.7 To download and install the version got to the python page [here](https://www.python.org/downloads/).


### Install libraries

This project uses third parthies python libs.
Make sure you have it all installed in your enviroment.
```
pip install -r requirements-prod.txt
```

## Deploy
```
sls deploy
```