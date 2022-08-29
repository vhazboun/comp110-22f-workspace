"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730465342"

five_letter: str = input("Enter a 5-character word: ")

if len(five_letter) == 5:
    one_character: str = input("Enter a single character: ")
else:
        print("Error: Word must contain 5 characters")
        exit()
if len(one_character) != 1:
        print("Error: Character must be a single character.")
        exit()

print("Searching for " + one_character + " in " + five_letter)


if one_character == five_letter[0]:
    print(one_character + " found at index 0")
if one_character == five_letter[1]:
    print(one_character + " found at index 1")
if one_character == five_letter[2]:
    print(one_character + " found at index 2")
if one_character == five_letter[3]:
    print(one_character + " found at index 3")
if one_character == five_letter[4]:
    print(one_character + " found at index 4")

matchy: int = 0
if one_character == five_letter[0]:
    matchy = matchy + 1
if one_character == five_letter[1]:
    matchy = matchy + 1
if one_character == five_letter[2]:
    matchy = matchy + 1
if one_character == five_letter[3]:
    matchy = matchy + 1
if one_character == five_letter[4]:
    matchy = matchy + 1

if matchy == 1:
    print(str(matchy) + " instance of " + one_character + " found in " + five_letter)
else:
    if matchy > 1:
        print(str(matchy) + " instances of " + one_character + " found in " + five_letter)
    else:
        print("No instances of " + one_character + " found in " + five_letter)






