from cs50 import get_string
import sys

test = "HELLO"
print(test.casefold())

def main():
    #Take a command line argument of the name/path of a dictionary of banned words
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)
    dictionary = sys.argv[1]

    dictionary_words = []

    f = open(dictionary)
    for word in f.read().split():
        dictionary_words.append(word)
    print(dictionary_words)

    message = get_string("What message would you like to censor? ")

    for word in message.split():
        if word.casefold() in dictionary_words:
            x = len(word)
            for i in range(x):
                print("*", end="")
            print(" ", end="")
        else:
            print(word, end=" ")

    print()

main()