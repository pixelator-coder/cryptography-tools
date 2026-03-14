# CAESAR CIPHER
# import caesar_cipher

# plaintext = caesar_cipher.get_plaintext()
# ciphertext = caesar_cipher.get_encrypted_string(plaintext)
# print(ciphertext)

# decrypted_text = caesar_cipher.get_decrypted_string(ciphertext)
# print(decrypted_text)

#RAIL FENCE TRANSPOSITION
import rail_fence_transposition

original_text = input("Enter original text: ")
transposed_text = rail_fence_transposition.get_transposed_string(original_text)
print(transposed_text)

untransposed_text = rail_fence_transposition.get_original_string(transposed_text)
print(untransposed_text)