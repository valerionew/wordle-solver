# words stolen from the original wordle code

# Open the list of words

with open("semplici.txt", "r") as dictionary:
    lines = dictionary.readlines()

# Select only 5 letter words and strip the newline
fiveletterwords = []
for word in lines:
    if len(word) == 6:  # only words with 5 letters + \n
        fiveletterwords.append(word.strip())

# calculate the a-priori probability
probabilities = [[0 for _ in range(26)] for _ in range(5)]
for word in fiveletterwords:
    for x, letter in enumerate(word):
        probabilities[x][ord(letter) - 97] += 1

# calculate probabilities for each word
wordprobabilities = {}
for word in fiveletterwords:
    wordprobabilities[word] = 1
    for x, letter in enumerate(word):
        if word.count(letter) > 1:
            # we discourage repetitions of letters 
            wordprobabilities[word] *= probabilities[x][ord(letter) - 97] / 2
        else:
            wordprobabilities[word] *= probabilities[x][ord(letter) - 97]


# pick the word with max probability: we could also take into account the non-repetition of letters to gain quickly insights
apriori = max(wordprobabilities, key=wordprobabilities.get)
print(apriori, wordprobabilities[apriori])

def userinput():
    while True:  # get a code from the user: this way sucks
        rawinput = input("Put 0 where grey, put 1 where yellow, put 2 where green: ")
        if len(rawinput) != 5:
            continue
        for char in rawinput:
            if char not in ["0", "1", "2"]:
                continue
        return rawinput

def wordtest(solution:list, guess:str ) -> str:
    solution = list(solution)
    guess = list(guess)
    test = ["0" for _ in range(5)]
    # we first find the greens and remove them from the word, this is for the correct handling of multiple occurrence
    for i,char in enumerate(guess):
        if char == solution[i]:
            test[i] = "2"
            guess[i] = "_"
            solution[i] = "-"

    # now we check the yellows: what should we do for multiple occurrence of a yellow char? set all to yw?
    for i,char in enumerate(guess):
        if char in solution:
            test[i] = "1"
    returnstr = ""
    for x in test:
        returnstr += x
    return returnstr




def getguess(words: list[str]) -> str:
    
    # ! should we calculate this every time? one simple try with today's italian word suggest that it could make the performance worse. I want to montecarlo this
    
    probabilities = [[0 for _ in range(26)] for _ in range(5)]
    for word in words:
        for x, letter in enumerate(word):
            probabilities[x][ord(letter) - 97] += 1
          
    wordprobabilities = {}
    for word in words:
        wordprobabilities[word] = 1
        for x, letter in enumerate(word):
            if word.count(letter) > 1:
                # we discourage repetitions of letters 
                wordprobabilities[word] *= probabilities[x][ord(letter) - 97] / 2
            else:
                wordprobabilities[word] *= probabilities[x][ord(letter) - 97]
    return max(wordprobabilities, key=wordprobabilities.get)


while True:
    rawinput = userinput()
    for i, char in enumerate(apriori):
        cleared = []
        for word in fiveletterwords:
            if rawinput[i] == "0":  # deletion logic
                # TODO: this could be impoved. We can delete this same letter in every position IF AND ONLY IF is present only once in the guess. If it is present more than once, we can delete it only if in all other position is gray. If it's yellow in the other position, we can delete only the words with that letter in the position we are testing right now. If it's green, we can delete the letter in ALL the other positions, except the green one. We should also take into account that we could have more than two repetitions of the same letter in the same word.
                if word[i] == char:
                    continue
                else:
                    cleared.append(word)
            elif rawinput[i] == "1":
                # we keep all the words not containing this letter and the words containng this letter at this position
                if char in word and word[i] != char:
                    cleared.append(word)
                else:
                    continue
            elif rawinput[i] == "2":
                # we delete all the words not containing this letter in this position
                if word[i] == char:
                    cleared.append(word)
                else:

                    continue
        fiveletterwords = cleared

    apriori = getguess(fiveletterwords);
    print(apriori)
