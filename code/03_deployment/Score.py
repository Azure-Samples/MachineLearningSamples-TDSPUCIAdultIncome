from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema
from azureml.logging import get_azureml_logger
import pandas
import pickle

def init():   
    # read in the model file
    ## Location of Model files 
    RandomForest_model_file = 'CVRandomForestModel.pkl'
    from sklearn.externals import joblib
    global model
    model = joblib.load(RandomForest_model_file)
        
def run(input_df):
    import json
    input = input_df.as_matrix()
    try:
            pred = model.predict(input)
            return json.dumps(str(pred[0]))
    except Exception as e:
        return (str(e))

####################
#  Main function
####################
if __name__ == '__main__':
    
    init()
    X_str =  '[{"capital_loss":-0.219095674,"hours_per_week":0.7559573744,"education_num":-0.4507068474,"capital_gain":-0.1480462751,"age":-0.0311032178,"Federal-gov":0.0,"Local-gov":0.0,"Private":1.0,"Self-emp-inc":0.0,"Self-emp-not-inc":0.0,"State-gov":0.0,"Without-pay":0.0,"Divorced":0.0,"Married-AF-spouse":0.0,"Married-civ-spouse":1.0,"Married-spouse-absent":0.0,"Never-married":0.0,"Separated":0.0,"Widowed":0.0,"Adm-clerical":0.0,"Armed-Forces":0.0,"Craft-repair":0.0,"Exec-managerial":0.0,"Farming-fishing":1.0,"Handlers-cleaners":0.0,"Machine-op-inspct":0.0,"Other-service":0.0,"Priv-house-serv":0.0,"Prof-specialty":0.0,"Protective-serv":0.0,"Sales":0.0,"Tech-support":0.0,"Transport-moving":0.0,"Husband":1.0,"Not-in-family":0.0,"Other-relative":0.0,"Own-child":0.0,"Unmarried":0.0,"Wife":0.0,"Amer-Indian-Eskimo":0.0,"Asian-Pac-Islander":0.0,"Black":0.0,"Other":0.0,"White":1.0,"Female":0.0,"Male":1.0,"Canada":0.0,"El-Salvador":0.0,"Germany":0.0,"Mexico":0.0,"Philippines":0.0,"Puerto-Rico":0.0,"United-States":1.0}]'
    X_test = pandas.read_json(X_str)
    # Get predictions
    y_pred = run(X_test)
    
    inputs = {"input_df": SampleDefinition(DataTypes.PANDAS, X_test)}
    # The prepare statement writes the scoring file (main.py) and
    # the schema file (service_schema.json) the the output folder.
    generate_schema(run_func=run, inputs=inputs, filepath = 'service_schema.json')
    logger = get_azureml_logger()
    logger.log("amlrealworld.uciincome.score", "true")
