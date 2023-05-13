from encryption import AESCipher

with open("key.bin", "rb") as f:
    key = f.read()

cipher = AESCipher(key)

plaintext = b"Hello, world!"
print("Plaintext:", plaintext)

ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
