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

def count_neighboring_letters(ciphertext, letter):
    num_neighboring_letters = 0
    num_repeats_itself = 0
    for ord in range(97,122,1):
        if letter + chr(ord) in ciphertext and letter == chr(ord):
            num_neighboring_letters += 1
            num_repeats_itself += 1
        elif letter + chr(ord) in ciphertext:
            num_neighboring_letters += 1
        elif chr(ord) + letter in ciphertext:
            num_neighboring_letters += 1
    print(f"{letter} neighbors " + str(num_neighboring_letters) + " letters.")
    print(f"{letter} repeats itself " + str(num_repeats_itself) + " times.")

count_neighboring_letters(ciphertext, most_common_letter)
count_neighboring_letters(ciphertext, second_most_common_letter)
count_neighboring_letters(ciphertext, third_most_common_letter)
