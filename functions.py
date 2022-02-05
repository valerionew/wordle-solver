import string

def wordtest(solution: list, guess: str) -> str:
    solution = list(solution)
    guess = list(guess)
    test = ["0" for _ in range(5)]
    # we first find the greens and remove them from the word, this is for the correct handling of multiple occurrence
    for i, char in enumerate(guess):
        if char == solution[i]:
            test[i] = "2"
            guess[i] = "_"
            solution[i] = "-"

    # now we check the yellows: what should we do for multiple occurrence of a yellow char? set all to yw?
    for i, char in enumerate(guess):
        if char in solution:
            test[i] = "1"
    returnstr = ""
    for x in test:
        returnstr += x
    return returnstr


def userinput():
    while True:  # get a code from the user: this way sucks
        rawinput = input("Put 0 where grey, put 1 where yellow, put 2 where green: ")
        if len(rawinput) != 5:
            continue
        for char in rawinput:
            if char not in ["0", "1", "2"]:
                continue
        return rawinput


def getguess(words: list[str]) -> str:
    #* STRATEGY: if we guessed 4 out of 5 letter and we have many words with those 4 letters, a better strategy could be trying to eliminate more letters instead of making many attempts changing just that letter.

    probabilities = letterprobabilities(words)

    wordprobabilities = {}

    for word in words:
        sum = 0
        for x, letter in enumerate(word):
            # ? should we discourage repetitions of letters?
            sum += probabilities[x][letter]  


        wordprobabilities[word] = sum
    return max(wordprobabilities, key=wordprobabilities.get)


def letterprobabilities(words):
    probabilities = [dict.fromkeys(string.ascii_lowercase, 0) for _ in range(5)]
    # wouldn't a dictionary be better than ord(letter)-97? YES!!!
    for word in words:
        for x, letter in enumerate(word):
            probabilities[x][letter] += 1
    return probabilities


def eliminator(thisroundwords, apriori, rawinput):
    #* PERFORMANCE: can this be rewritten so that it doesn't cycle through EVERY WORD 5 TIMES?
    for i, char in enumerate(apriori):
        cleared = []
        for word in thisroundwords:
            if rawinput[i] == "0":  # deletion logic
                # TODO: this could be impoved. We can delete this same letter in every position IF AND ONLY IF is present only once in the guess. If it is present more than once, we can delete it only if in all other position is gray. If it's yellow in the other position, we can delete only the words with that letter in the position we are testing right now. If it's green, we can delete the letter in ALL the other positions, except the green one. We should also take into account that we could have more than two repetitions of the same letter in the same word.
                if word.count(char) > apriori.count(char):
                    if word[i] == char:
                        continue
                    else:
                        cleared.append(word)
                elif word.count(char) == apriori.count(char):  
                    #! the only one but we should check also that all are 0
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
        thisroundwords = cleared
    return thisroundwords
