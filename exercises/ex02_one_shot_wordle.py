"""EX01 - One Shot Wordle."""

__author__ = "730465342"

secret: str = "python"

word_le: str = input(f"What is your { str(len(secret)) } letter guess? ")

while len(word_le) != len(secret):
    word_le: str = input(f"That was not { str(len(secret)) } letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
yi: int = 0
end: int = int(len(word_le))
blocks: str = ""
check: bool = False

while i < end:
    if word_le[i] == secret[i]:
        blocks += str(GREEN_BOX)
    else:
        while check is not True and yi < end:
            if word_le[i] == secret[yi]:
                check = True
                blocks += str(YELLOW_BOX)
            else:
                yi += 1
        if check is False:
            blocks += str(WHITE_BOX)
        yi = 0
    check = False
    i += 1

print(blocks)

if word_le == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

