#I don't want to write a game because I'm not that into video games.
#input text file as a command line argument
import random
vocabdict = {}

def create_vocab_dict(txtfile):
    vocabtxt = open(txtfile)
    nextvocab = vocabtxt.readline().strip("\n")
    print(nextvocab)
    while nextvocab != "":
        key, value = nextvocab.split(", ", 1)
        vocabdict[key] = value
        nextvocab = vocabtxt.readline().strip("\n")

print("""Welcome to the vocab game!
        Please enter the text file that contains your vocabulary.
        Vocab words should be separated from their definitions by a comma.
        """)
txtfile = input("> ")
create_vocab_dict(txtfile)
print("""Would you like to be shown the vocab,
        the definitions, or a mixture of both?
        """)
choice = input("> ")
keys = list(vocabdict.keys())
random.shuffle(keys)

def guess_vocab(current):
    print(f"Your vocab word is {current}.")
    input("Please type your definition: ")
    print("Here is the definition we have on file:")
    print(vocabdict[current])
    print("Did you answer correctly?")

def guess_definitions(current):
    print(f"Please give us the vocab word that matches this definition: {vocabdict[current]}")
    input("> ")
    print(f"The correct vocab word is: {current}")
    print("Did you answer correctly?")

def correct_or_naw(current):
    response = input("> ")
    if response == "no":
        print("That's too bad! We will retest you on this later.")
        keys.insert(0, current)
    else:
        print("Great job! We won't test you on that again.")


def vocab(txtfile):
    while keys:
        current = keys.pop()
        guess_vocab(current)
        correct_or_naw(current)

def definitions(txtfile):
    while keys:
        current = keys.pop()
        guess_definitions(current)
        correct_or_naw(current)

def mixture(txtfile):
    while keys:
        current = keys.pop()
        guess_vocab(txtfile, current)
        correct_or_naw(current)
        if keys:
            current = keys.pop()
            guess_definitions(txtfile, current)
            correct_or_naw(current)

def begin(choice):
    if choice == "vocab":
        print("Let's do this")
        vocab(vocabdict)
    elif choice == "definitions":
        definitions(vocabdict)
    elif "mixture" in choice:
        mixture(vocabdict)
    else:
        print("Please type 'vocab', 'definitions', or 'mixture'")
        choice = input("> ")
        begin(choice)

begin(choice)

#next, make it work with a comma separated txt file! How do I do that?
