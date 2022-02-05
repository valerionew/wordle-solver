# words stolen from the original wordle code
from functions import *

# Open the list of words


with open("easy.txt", "r") as dictionary:
    lines = dictionary.readlines()

# Select only 5 letter words and strip the newline
thisroundwords = [s.strip() for s in lines]


while True:
    apriori = getguess(thisroundwords);
    print(apriori)
    rawinput = userinput()
    thisroundwords = eliminator(thisroundwords,apriori,rawinput)
