import random

keytext = "Three rings for the Elven-lords under the sky, Seven for  the  Dwarf-lords  in  their  halls  of  stone,  Nine  for  Mortal  Men  doomed  to  die, One  for  the  Dark  Lord  on  his  dark  throne In the Land of Mordor  where  the  Shadows  lie. One  Ring  to  rule  them  all,  One  Ring  to  find  them, One  Ring  to  bring  them  all  and  in  the  darkness  bind  them In  the  Land  of  Mordor  where  the  Shadows  lie."

letter_to_num_map = {"e": [2, 18, 24, 30], "m": [3, 5, 10]}
plaintext = "mememe"
plaintext_as_list = list(plaintext)
def letter_to_number(letter):
    replacement_index = random.randint(0, len(letter_to_num_map[letter]) - 1)
    replacement_number = letter_to_num_map[letter][replacement_index]
    return replacement_number
    
ciphertext = map(letter_to_number, plaintext)
print(list(ciphertext))