import os
from dotenv import load_dotenv

from src.kafka_config import API_KEY, ENV_PATH

# ENV_PATH = os.path.join(os.getcwd(), "Project-1_Sensor_Fault_Detection", "ml_data_pipeline", "conf", ".env")
ENV_PATH = r"F:\Data-Science-Projects\Project-1_Sensor_Fault_Detection\ml_data_pipeline\src\conf\.env"
print(ENV_PATH)

load_dotenv(ENV_PATH)

API_KEY = os.getenv('API_KEY', None)
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY', None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', None)
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL', None)
SSL_MACHENISM = os.getenv('SSL_MACHENISM', None)
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY', None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', None)

print(API_KEY)
