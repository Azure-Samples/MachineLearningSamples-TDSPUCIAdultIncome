# code\/03_deployment

We provide information about each of the files used for deployment.

## Score.py
    Purpose: generate necessary artifacts (JSON) schema used in operationalization
    Language: Python
    How it gets used: used in deployment
    init: load machine learning model 
    run: >Python Score.py

## How to operationalize
    1. Copy generated model file from previous step to the project root directory
    2. Copy Score.py to the project root directory
    3. Under project root directory, run Score.py to generate service_schema.json
    4. Set up operationalization environment
    5. Run the following command from project root to deploy 
    >az ml service create realtime -f Score.py --model-file CVRandomForestModel.pkl -s service_schema.json -n <app_name> -r python
