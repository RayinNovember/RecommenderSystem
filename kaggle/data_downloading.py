import kagglehub
import os
import shutil
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

os.environ['KAGGLE_API_TOKEN'] = os.getenv('KAGGLE_API_TOKEN')
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)
path = kagglehub.dataset_download("ra4u12/bookrecommendation")
print("Downloaded to:", path)

# Copy files from cache to your project's data folder
for file in os.listdir(path):
    shutil.copy(os.path.join(path, file), DATA_DIR)

print("Copied to:", DATA_DIR)