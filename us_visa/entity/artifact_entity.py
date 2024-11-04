# artifact entity means the return type of the particular component.
# What data ingestion will return as an artifact ?
# it will return train and test csv files.
# We are working on the data ingestion component. and how many files will your data ingestion component will return for the next component.
# 2 files.
# our next component is data validation. to validate the data what we need. We need train and test file.
# and this files we will get from data ingestion component.
# validation will return true if dataset is fine. once we get the true message. Our next component will start --> transforamation.
# transformation will return you the cleaned data.
# Once you get cleaned data, ur next component "model_trainer" will start. Model trainer will take cleaned data from previous compoenet.
# once training is completed, model trainer will return the trained model.
# our next component will be model_evaluation. Model evaluation will take trained model and test data from previous component.
# So on each compoent will depend on other component.
# Suppose if one component fails, then the whole pipeline will fail.
# for each component, there will a artifact that it will return.

# ****These all components create the pipeline****.
# Whatever component we write, that component will return something and that return we will as input for the next component.
# ML pipeline is like a chain of components.


from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 


@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str
