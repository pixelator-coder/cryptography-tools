ciphertext = "pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
char_count = {}
for character in ciphertext:
    char_count[character] = char_count.get(character, 0) + 1
sorted_dict = dict(sorted(char_count.items()))
for character, count in sorted_dict.items():
    print(character + f"{count:>5}")