import caesar_cipher

plaintext = caesar_cipher.get_plaintext()
ciphertext = caesar_cipher.get_encrypted_string(plaintext)
print(ciphertext)

decrypted_text = caesar_cipher.get_decrypted_string(ciphertext)
print(decrypted_text)