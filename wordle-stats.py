# words stolen from the original wordle code

# Open the list of words

with open("fiveletterwords.txt", "r") as dictionary:
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
        wordprobabilities[word] *= probabilities[x][ord(letter) - 97]

# pick the word with max probability: we could also take into account the non-repetition of letters to gain quickly insights
apriori = max(wordprobabilities, key=wordprobabilities.get)
print(apriori, wordprobabilities[apriori])


#
while True:
    while True:  # get a code from the user: this way sucks
        rawinput = input("Put 0 where grey, put 1 where yellow, put 2 where green: ")
        if len(rawinput) != 5:
            continue
        for char in rawinput:
            if char not in ["0", "1", "2"]:
                continue
        break
    for i, char in enumerate(apriori):
        cleared = []
        for word in fiveletterwords:
            if rawinput[i] == "0":  # deletion logic
                # if the marked 0 char is the only one in the word, we can safely delete it and adios
                if word[i] == char:
                    continue
                else:
                    cleared.append(word)
            elif (
                rawinput[i] == "1"
            ):  # we keep all the words not containing this letter and the words containng this letter at this position
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

    wordprobabilities = {}

    for word in fiveletterwords:
        wordprobabilities[word] = 1
        for x, letter in enumerate(word):
            wordprobabilities[word] *= probabilities[x][ord(letter) - 97]

    apriori = max(wordprobabilities, key=wordprobabilities.get)
    print(apriori, wordprobabilities[apriori])
