# words stolen from the original wordle code

# Open the list of words
with open('fiveletterwords.txt', 'r') as dictionary:
    lines = dictionary.readlines()

# Select only 5 letter words and strip the newline
fiveletterwords = []
for word in lines:
    if len(word) == 6: # only words with 5 letters + \n
        fiveletterwords.append(word.strip())

# calculate the a-priori probability 
probabilities = [[0 for _ in range(26)] for _ in range(5)]
for word in fiveletterwords:
    for x,letter in enumerate(word):
        probabilities[x][ord(letter)-97] += 1

# calculate probabilities for each word
wordprobabilities = {}
for word in fiveletterwords:
    wordprobabilities[word] = 1
    for x,letter in enumerate(word):
        wordprobabilities[word] *= probabilities[x][ord(letter)-97]

# pick the word with max probability: we could also take into account the non-repetition of letters to gain quickly insights
apriori = max(wordprobabilities, key=wordprobabilities.get)
print(apriori)

# 
greens = [0 for _ in range(5)]
# 
while True:
    while True:
        rawinput = input("Put 0 where grey, put 1 where yellow, put 2 where green: ")
        if len(rawinput) != 5:
            continue
        for char in rawinput:
            if char not in ['0','1','2']:
                continue
        break

    for iterator,value in enumerate(rawinput):
        if value == '2':
            greens[iterator] = apriori[iterator]

    for i,char in enumerate(apriori):
        cleared = []
        if rawinput[i] == '0': # we delete all the words containing this letter
            for word in fiveletterwords: 
                # DEBUG
                if word == "light":
                    ...

                if char in word and (not (char in greens)): 
                    # special case handling: if we get a gray AFTER we got a green for another position, we are sure that the letter will be ONLY in the green position and not anywhere else in the word, but the word
                    continue
                else:
                    cleared.append(word)
        elif rawinput[i] == '1': # we delete all the words not containing this letter
            for word in fiveletterwords:
                if char in word:
                    if word[i] != char:
                        cleared.append(word)
                else:
                    continue
        elif rawinput[i] == '2': # we delete all the words not containing this letter in this position
            
            for word in fiveletterwords:
                if word[i] == char:
                    cleared.append(word)
                else:
                    continue
        fiveletterwords = cleared
    
    wordprobabilities = {}

    for word in fiveletterwords:
        wordprobabilities[word] = 1
        for x,letter in enumerate(word):
            wordprobabilities[word] *= probabilities[x][ord(letter)-97]

    apriori = max(wordprobabilities, key=wordprobabilities.get)

    print(apriori)




    
...
