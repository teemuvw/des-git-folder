import pytest
from des import des_encrypt

def test_des_basic():
    plaintext = "11111111"
    key = "11111111"
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16
def test_des_plaintext_padding():
    # Plaintext shorter than 8 bytes
    plaintext = "1234"
    key = "abcdefgh"
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16   
def test_des_key_padding():
    # Plaintext shorter than 8 bytes
    plaintext = "secretzz"
    key = "1234"
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16   