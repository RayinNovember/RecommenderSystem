import os
import sys
import kagglehub
import shutil
from dotenv import load_dotenv
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration

class DataIngestion:
    
    def __init__(self, config: AppConfiguration):
        try:
            logging.info("Data Ingestion component initialized")
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            load_dotenv(os.path.join(BASE_DIR, ".env"))
            os.environ['KAGGLE_API_TOKEN'] = os.getenv('KAGGLE_API_TOKEN')
            self.data_ingestion_config = config
        except Exception as e:
            raise AppException(e, sys) from e

    def download_data(self):
        try:
            cache_path = kagglehub.dataset_download("ra4u12/bookrecommendation")
            logging.info("Downloaded to:", cache_path)
            ingested_data_dir = self.data_ingestion_config.get_data_ingestion_config().ingested_dir

            # Copy files from cache to your project's data folder
            for file in os.listdir(cache_path):
                shutil.copy(os.path.join(cache_path, file), ingested_data_dir)
            logging.info("Copied to:", ingested_data_dir)
            
        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion")
            self.download_data()
            logging.info("Data ingestion completed")
        except Exception as e:
            raise AppException(e, sys) from e