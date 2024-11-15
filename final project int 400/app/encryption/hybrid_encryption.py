import os
from .aes_encryption import aes_encrypt, aes_decrypt
from .ecc_encryption import ecc_keypair, ecc_encrypt, ecc_decrypt

def hybrid_encrypt(plaintext):
    aes_key = os.urandom(32)  # 256-bit AES key
    iv, ciphertext = aes_encrypt(aes_key, plaintext)

    ecc_priv_key, ecc_pub_key = ecc_keypair()

    # Convert aes_key to integer for ECC encryption
    aes_key_int = int.from_bytes(aes_key, 'big')
    encrypted_aes_key = ecc_encrypt(aes_key_int, ecc_pub_key)

    return iv, ciphertext, encrypted_aes_key, ecc_pub_key


def hybrid_decrypt(iv, ciphertext, encrypted_aes_key, ecc_priv_key):
    aes_key = ecc_decrypt(encrypted_aes_key, ecc_priv_key)
    plaintext = aes_decrypt(aes_key, iv, ciphertext)
    return plaintext
from tinyec import registry

def deserialize_public_key(public_key_data):
    curve = registry.get_curve('brainpoolP256r1')
    x = int(public_key_data['x'])
    y = int(public_key_data['y'])
    return curve.point(x, y)
