ciphertext = "pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
char_count = {}
total_count = 0
for character in ciphertext:
    if ord(character) < 97 or ord(character) > 122:
        continue
    char_count[character] = char_count.get(character, 0) + 1
    total_count += 1
sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
letters_sorted_by_count = list(sorted_dict.keys())
most_common_letter = letters_sorted_by_count[0]
second_most_common_letter = letters_sorted_by_count[1]
third_most_common_letter = letters_sorted_by_count[2]
print("Most common letter: " + most_common_letter)
print("Second most common letter: " + second_most_common_letter)
print("Third most common letter: " + third_most_common_letter)

num_neighboring_letters = 0
for ord in range(97,122,1):
    if most_common_letter + chr(ord) in ciphertext:
        print("yes " + most_common_letter + chr(ord))
        num_neighboring_letters += 1
    elif chr(ord) + most_common_letter in ciphertext:
        print("yes " + chr(ord) + most_common_letter)
        num_neighboring_letters += 1
    else:
        print("no")
print("The most common letter neighbors " + str(num_neighboring_letters) + " letters.")

num_neighboring_letters = 0
for ord in range(97,122,1):
    if second_most_common_letter + chr(ord) in ciphertext:
        print("yes " + second_most_common_letter + chr(ord))
        num_neighboring_letters += 1
    elif chr(ord) + second_most_common_letter in ciphertext:
        print("yes " + chr(ord) + second_most_common_letter)
        num_neighboring_letters += 1
    else:
        print("no")
print("The 2nd most common letter neighbors " + str(num_neighboring_letters) + " letters.")

num_neighboring_letters = 0
for ord in range(97,122,1):
    if third_most_common_letter + chr(ord) in ciphertext:
        print("yes " + third_most_common_letter + chr(ord))
        num_neighboring_letters += 1
    elif chr(ord) + third_most_common_letter in ciphertext:
        print("yes " + chr(ord) + third_most_common_letter)
        num_neighboring_letters += 1
    else:
        print("no")
print("The 3rd most common letter neighbors " + str(num_neighboring_letters) + " letters.")