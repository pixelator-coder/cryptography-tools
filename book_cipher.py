import random

# Section 1: Encryption
keytext = input("Enter keytext: ")
keytext_lowered = keytext.lower()

keytext_clean = keytext_lowered.replace("-", " ")
keytext_list = keytext_clean.split()
letter_to_num_map = {}
for index, word in enumerate(keytext_list):
    first_letter = word[0]
    if first_letter in letter_to_num_map:
        letter_to_num_map[first_letter].append(index + 1)
    else:
        letter_to_num_map[first_letter] = [index + 1]

plaintext = input("Enter plaintext: ")
plaintext_as_list = list(plaintext)
def letter_to_number(letter):
    if letter not in letter_to_num_map:
        return letter
    number_list = letter_to_num_map[letter]
    replacement_index = random.randint(0, len(number_list) - 1)
    replacement_number = number_list[replacement_index]
    return replacement_number
    
ciphertext = map(letter_to_number, plaintext)
list_ciphertext = list(ciphertext)
print(list_ciphertext)

# Section 2: Decryption

recovered_plaintext = ""
for replacement_character in list_ciphertext:
    found_in_map = False
    for letter in letter_to_num_map:
        if replacement_character in letter_to_num_map[letter]:
            recovered_plaintext += letter
            found_in_map = True
            break
    if not found_in_map:
        recovered_plaintext += replacement_character

print("The original plaintext is: " + plaintext)
print("The recovered plaintext is: " + recovered_plaintext)