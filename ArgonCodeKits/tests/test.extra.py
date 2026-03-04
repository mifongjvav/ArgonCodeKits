from ArgonCodeKits import encrypt, decrypt

def test_encrypt_decrypt():
    original = "Hello Argon"
    password = "secret"

    cipher = encrypt(original, password)
    result = decrypt(cipher, password)

    assert result == original