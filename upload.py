import os
import pandas as pd
from pymongo import MongoClient

class MongoIO:
    def __init__(self, client_url, database_name, collection_name):
        # Initialize MongoDB client and specify the collection
        self.client = MongoClient(client_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def bulk_insert(self, csv_file_path):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert DataFrame to a list of dictionaries (one per row)
        data = df.to_dict(orient='records')

        # Perform bulk insert into MongoDB collection
        if data:
            result = self.collection.insert_many(data)
            print(f"Inserted {len(result.inserted_ids)} documents into {self.collection.name}.")
        else:
            print(f"No data to insert from {csv_file_path}")

def upload_files_to_mongodb(mongo_client_con_string, database_name, datasets_dir_name):
    for file in os.listdir(datasets_dir_name):
        if file.endswith('.csv'):  # Process only CSV files
            file_name = file.split('.')[0]  # Remove file extension to use as collection name

            # Establish MongoDB connection for each CSV file
            mongo_connection = MongoIO(
                client_url=mongo_client_con_string,
                database_name=database_name,
                collection_name=file_name  # Use the base file name as the collection name
            )

            # Construct the full file path
            file_path = os.path.join(datasets_dir_name, file)
            print(f"Processing file: {file_path}")
            
            # Perform the bulk insert operation
            mongo_connection.bulk_insert(file_path)

            print(f"{file_name} is uploaded to MongoDB")

# Example usage: Update the following variables as needed
client_url = "mongodb+srv://priyanka369runa97531:_priyanka_123_@workflow.cusps.mongodb.net/?retryWrites=true&w=majority&appName=WorkFlow"
database_name = "Phishing"  # MongoDB database name
datasets_dir_name = r"G:\PROJECT3_PHISHING_CLASSIFIERS\upload_data_to_db"  # Directory containing the CSV files

# Call the function to upload files
upload_files_to_mongodb(
    mongo_client_con_string=client_url,
    database_name=database_name,
    datasets_dir_name=datasets_dir_name
)
