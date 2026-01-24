# Collecting, loading, and storing raw data so it can be used for training and prediction in your ML pipeline.
# Bringing data into your system from some source

#data_ingestion.py can load data from:

# CSV / Excel files
# Databases (MySQL, MongoDB, PostgreSQL)
# APIs
# Cloud storage (S3, Azure Blob, GCP)
# Real-time streams (Kafka, sensors)

# Fetch Data
# Validate Data
# Split Data


import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
 
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


# This class stores FILE PATHS
# Think of this as a "settings box
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact','train.csv') #Where to save the training file
    test_data_path: str = os.path.join('artifact','test.csv') #Where to save the testing file
    raw_data_path: str = os.path.join('artifact','data.csv') #Where to save the raw file


# This class performs the actual data ingestion work
class DataIngestion:
    def __init__(self):
        # Create an object of the config class
        # Now we can access all file paths easily
        self.ingestion_config = DataIngestionConfig()

    # Main method to run the data ingestion process
    def initiate_data_ingestion(self):
        # Log that this function has started
        logging.info("Entered the data ingestion component")

        try:
            # Step 1: Read the raw dataset from CSV file
            df = pd.read_csv('notebook\\data\\stud.csv')
            logging.info("Dataset read into pandas DataFrame")

            # Step 2: Create the artifact folder if it doesn't exist
            # This is where all output files will be stored
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # Step 3: Save a copy of the raw data
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )
            logging.info("Raw data saved")

            # Step 4: Split data into training and testing sets
            # 80% for training, 20% for testing
            logging.info("Train-test split started")
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Step 5: Save training data to CSV
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            # Step 6: Save testing data to CSV
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Data ingestion completed successfully")

            # Step 7: Return file paths for next pipeline steps
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        # If anything goes wrong, raise a custom error
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
