# code\/03_deployment

We provide information about each of the files used for deployment.

## Score.py
    Purpose: generate necessary artifacts (JSON) schema used in operationalization
    Language: Python
    How it gets used: used in deployment
    init: load machine learning model 
    run: predict with machine learning model

## How to operationalize
    Copy generated model file from previous step to the project root directory
    Copy Score.py to the project root directory
    Run Score.py to generate service_schema.json
    Set up cluster
    Run the following command to deploy >az ml service create realtime -f Score.py --model-file CVRandomForestModel.pkl -s service_schema.json -n <app_name> -r python
