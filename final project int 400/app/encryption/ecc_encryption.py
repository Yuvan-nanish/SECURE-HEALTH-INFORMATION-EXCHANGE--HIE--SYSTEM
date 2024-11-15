import os
from tinyec import registry
from hashlib import sha256

def ecc_keypair():
    curve = registry.get_curve('brainpoolP256r1')
    priv_key = int.from_bytes(os.urandom(32), 'big') % curve.field.n  # Convert bytes to integer
    pub_key = priv_key * curve.g
    return priv_key, pub_key


def ecc_encrypt(aes_key, ecc_pub_key):
    shared_key = ecc_pub_key * aes_key  # aes_key should be an integer
    return sha256(int.to_bytes(shared_key.x, 32, 'big')).digest()


def ecc_decrypt(encrypted_aes_key, ecc_priv_key):
    shared_key = encrypted_aes_key * ecc_priv_key
    return sha256(int.to_bytes(shared_key.x, 32, 'big')).digest()



from tinyec import registry

from tinyec import registry

def deserialize_public_key(public_key_data):
    curve = registry.get_curve('brainpoolP256r1')
    x = int(public_key_data['x'])
    y = int(public_key_data['y'])
    return curve.point(x, y)  # This should correctly create a point on the curve



# Example usage within the file if needed for decryption:
# public_key = deserialize_public_key(retrieved_data['public_key'])
