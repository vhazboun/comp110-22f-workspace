from random import randint

question: str = input("Ask a yes/no question...")
response: int = randint(0, 5)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("You betcha")
elif response == 3:
    print("U already know mah slimeball g, GANGSTA")
elif response == 4:
    print("Yeeeeaaaaaahhhhhhh nah.")
else:
    print("My sources say no")