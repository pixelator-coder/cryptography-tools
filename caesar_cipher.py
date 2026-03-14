KEY = 2
ORD_OF_Z = 122
ORD_OF_A = 97
NUM_LETTERS = 26

def get_plaintext():
    print("Enter plaintext:")
    return input()

def get_encrypted_character(character):
    if ord(character) > ORD_OF_Z or ord(character) < ORD_OF_A:
        return character
    ordinal = ord(character) + KEY
    if ordinal > ORD_OF_Z:
        ordinal = ordinal - NUM_LETTERS
    encrypted_character = chr(ordinal)
    return encrypted_character

def get_encrypted_string(string):
    encrypted_string = ""
    for character in string:
        encrypted_character = get_encrypted_character(character)
        encrypted_string += encrypted_character
    return encrypted_string

def get_decrypted_character(character):
    if ord(character) > ORD_OF_Z or ord(character) < ORD_OF_A:
        return  character
    ordinal = ord(character) - KEY
    if ordinal < ORD_OF_A:
        ordinal = ordinal + NUM_LETTERS
    decrypted_character = chr(ordinal)
    return decrypted_character

def get_decrypted_string(string):
    decrypted_string = ""
    for character in string:
        decrypted_character = get_decrypted_character(character)
        decrypted_string += decrypted_character
    return decrypted_string