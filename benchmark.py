from functions import *

with open("easy.txt", "r") as dictionary:
    lines = dictionary.readlines()
# Select only 5 letter words and strip the newline
fiveletterwords = [s.strip() for s in lines]
"""
for word in lines:
    if len(word) == 6:  # only words with 5 letters + \n
        fiveletterwords.append(word.strip())
"""
score = [0 for _ in range(6)]
notguessed = []

for solution in fiveletterwords:
    thisroundwords = fiveletterwords

    for i in range(7):
        if i == 6:
            #print("cannot guess", solution)
            notguessed.append(solution)
            break

        apriori = getguess(thisroundwords);
    
        rawinput = wordtest(solution, apriori)

        if rawinput == "22222":
            # print("guessed ", solution, "in",i)
            score[i] += 1
            break

        if solution == "vesto":
            ...
        thisroundwords = eliminator(thisroundwords,apriori,rawinput)

print("score: ", score, "on: ", len(lines), "not guessed: ",len(notguessed), (notguessed))
