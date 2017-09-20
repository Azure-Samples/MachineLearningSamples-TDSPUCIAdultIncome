# code\/03_deployment

We provide information about each of the files used for deployment.

## Score.py
    Purpose: generate necessary artifacts (JSON) schema used in operationalization
    Language: Python
    How it gets used: used in deployment
    init: load machine learning model 
    run: predict with machine learning model


## service_schema.json
    Purpose: specify web service input data format
    Language: Python
    How it gets used: used in deploymnet


## How to operationalize
    Copy generated model file from previous step to the project root directory
    copy Score.py and service_schema.json to the project root directory
    Set up cluster
    Run az ml service create realtime -f Score.py --model-file CVRandomForestModel.pkl -s service_schema.json -n <app_name> -r python
