from pymongo import MongoClient

def view_encrypted_ehr():
    client = MongoClient('mongodb://localhost:27017/')  # Update if using a different connection string
    db = client['ehr_encryption']  # Replace with your database name
    collection = db['encrypted_ehr']  # Replace with your collection name

    # Retrieve and print all documents
    for document in collection.find():
        print(document)

if __name__ == "__main__":
    view_encrypted_ehr()
