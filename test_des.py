import pytest
from des import ascii_to_bits_in_list, pc1_permutation, generate_subkeys, xor_round_substitution, des_encrypt, shifts

# --- ascii_to_bits_in_list tests ---
def test_ascii_to_bits_basic():
    bits = ascii_to_bits_in_list(list("12345678"))
    assert isinstance(bits, list)
    assert len(bits) == 64
    assert all(bit in ["0", "1"] for bit in bits)

def test_ascii_to_bits_padding():
    bits = ascii_to_bits_in_list(list("1234"))
    assert len(bits) == 64  # Should pad to 8 bytes
    # Check that last byte is padding value 4 (0b00000100)
    last_byte = bits[-8:]
    assert last_byte == list("00000100")  

# --- pc1_permutation tests ---
def test_pc1_permutation_length():
    bits = ascii_to_bits_in_list(list("12345678"))
    permuted = pc1_permutation(bits)
    assert len(permuted) == 56

# --- generate_subkeys tests ---
def test_generate_subkeys_length():
    bits = ascii_to_bits_in_list(list("12345678"))
    permuted = pc1_permutation(bits)
    subkeys = generate_subkeys(permuted)
    assert len(subkeys) == 16
    assert all(len(k) == 48 for k in subkeys)

# --- xor_round_substitution tests ---
def test_xor_round_substitution_type():
    bits = ascii_to_bits_in_list(list("12345678"))
    permuted = pc1_permutation(bits)
    subkeys = generate_subkeys(permuted)
    ciphertext = xor_round_substitution(bits, subkeys)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16

# --- Full DES test ---
def test_des_encrypt_output():
    plaintext = list("12345678")
    key = list("abcdefgh")
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16

# --- Full DES test with key padding ---
def test_des_encrypt_key_padding_output():
    plaintext = list("12345678")
    key = list("shortk")
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16
# --- Full DES test with plaintext padding ---
def test_des_encrypt_input_padding_output():
    plaintext = list("1234")
    key = list("12345678")
    ciphertext = des_encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == 16