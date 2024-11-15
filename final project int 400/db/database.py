from pymongo import MongoClient
import os

def init_db():
    try:
        # Connect to MongoDB at localhost:27017
        client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        
        # Use the 'ehr_encryption' database
        db = client['ehr_encryption']
        
        # Access the 'encrypted_ehr' collection
        collection = db['encrypted_ehr']
        
        print("Connected to MongoDB database")
        return db, collection

    except Exception as e:
        print(f"Error: {e}")
        return None, None
