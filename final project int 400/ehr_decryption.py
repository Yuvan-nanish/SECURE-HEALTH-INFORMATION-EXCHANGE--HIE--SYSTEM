import json
from app.encryption.hybrid_encryption import hybrid_decrypt
from app.encryption.ecc_encryption import deserialize_public_key
from bson.binary import Binary

# Function to load encrypted data from a JSON file (or you can replace this with your method)
def load_encrypted_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Load encrypted data (update the path as needed)
    encrypted_data = load_encrypted_data('data/encrypted_data.json')

    # Extract the necessary components from the encrypted data
    serialized_pub_key = encrypted_data['ecc_pub_key']
    encrypted_aes_key = Binary(encrypted_data['encrypted_aes_key'], 0)
    ciphertext = Binary(encrypted_data['ciphertext'], 0)
    iv = Binary(encrypted_data['iv'], 0)

    # Deserialize the public ECC key
    ecc_pub_key = deserialize_public_key(serialized_pub_key)

    # Load the private key (assuming it's stored in a file)
    with open('data/keys/private_key.pem', 'r') as key_file:
        private_key = key_file.read()  # Adjust based on how the key is stored

    # Call the hybrid_decrypt function
    decrypted_data = hybrid_decrypt(ecc_pub_key, private_key, encrypted_aes_key, ciphertext, iv)

    # Print the decrypted data
    print("Decrypted EHR Data:", decrypted_data)

if __name__ == "__main__":
    main()
