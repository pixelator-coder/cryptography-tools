answer = input("Do you want to do it?")
while answer != "n":
    password = input("Enter a password using only letters: ")
    secret = 0
    for index, letter in enumerate(password):
        ordinal = ord(letter)
        secret += ordinal * (index + 1)

    print(secret % 100)
    answer = input("Do you want to do it?")