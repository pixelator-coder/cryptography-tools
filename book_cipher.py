import random

keytext = "Three rings for the Elven-lords under the sky, Seven for  the  Dwarf-lords  in  their  halls  of  stone,  Nine  for  Mortal  Men  doomed  to  die, One  for  the  Dark  Lord  on  his  dark  throne In the Land of Mordor  where  the  Shadows  lie. One  Ring  to  rule  them  all,  One  Ring  to  find  them, One  Ring  to  bring  them  all  and  in  the  darkness  bind  them In  the  Land  of  Mordor  where  the  Shadows  lie."
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

plaintext = "hello"
plaintext_as_list = list(plaintext)
def letter_to_number(letter):
    if letter not in letter_to_num_map:
        return letter
    number_list = letter_to_num_map[letter]
    replacement_index = random.randint(0, len(number_list) - 1)
    replacement_number = number_list[replacement_index]
    return replacement_number
    
ciphertext = map(letter_to_number, plaintext)
print(list(ciphertext))