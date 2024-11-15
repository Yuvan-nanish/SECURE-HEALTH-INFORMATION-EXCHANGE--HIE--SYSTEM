import json
from app.encryption.hybrid_encryption import hybrid_encrypt

def serialize_pub_key(pub_key):
    """Serialize the public key for storage."""
    return {
        'x': str(pub_key.x),  # Convert to string
        'y': str(pub_key.y)   # Convert to string
    }

def store_encrypted_ehr(encrypted_document, collection):
    """Store the encrypted EHR document in the MongoDB collection."""
    collection.insert_one(encrypted_document)

def encrypt_and_store_ehr(ehr_data, collection):
    """Encrypt the EHR data and store it in the database."""
    try:
        plaintext = json.dumps(ehr_data)

        # Perform hybrid encryption
        iv, ciphertext, encrypted_aes_key, ecc_pub_key = hybrid_encrypt(plaintext)

        # Prepare the encrypted document
        encrypted_document = {
            'iv': iv,
            'ciphertext': ciphertext,
            'encrypted_aes_key': encrypted_aes_key,
            'ecc_pub_key': serialize_pub_key(ecc_pub_key)  # Serialize public key here
        }

        # Store the encrypted EHR in the database
        store_encrypted_ehr(encrypted_document, collection)

    except Exception as e:
        print(f"An error occurred while encrypting and storing EHR: {e}")
