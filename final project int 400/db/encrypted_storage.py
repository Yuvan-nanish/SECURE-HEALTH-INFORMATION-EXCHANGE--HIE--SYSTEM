def store_encrypted_ehr(encrypted_document, collection):
    # Insert the encrypted document into the MongoDB collection
    collection.insert_one(encrypted_document)
