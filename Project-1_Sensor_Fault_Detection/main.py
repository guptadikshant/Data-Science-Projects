from sensor.configuration.mongo_db_connection import MongoDBClient

from sensor.entity.config_entitiy import TrainingPipelineConfig, DataIngestionConfig

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print(mongodb_client.database.list_collection_names())

    training_pipeline = TrainingPipelineConfig()
    data_ingestion = DataIngestionConfig(training_pipeline_config=training_pipeline)
    print(data_ingestion.__dict__)