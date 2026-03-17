ciphertext = "pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
char_count = {}
total_count = 0
for character in ciphertext:
    if ord(character) < 97 or ord(character) > 122:
        continue
    char_count[character] = char_count.get(character, 0) + 1
    total_count += 1
sorted_dict = dict(sorted(char_count.items()))
largest_count = 0
most_common_letter = ""
for letter, count in sorted_dict.items():
    percentage = count*100/total_count
    rounded_percentage = round(percentage, 1)
    print(letter + f"{count:>5}"+ f"{rounded_percentage:>7}")
    if count > largest_count:
        largest_count = count
        most_common_letter = letter
print("most common letter: " + most_common_letter + f"{largest_count:>5}")