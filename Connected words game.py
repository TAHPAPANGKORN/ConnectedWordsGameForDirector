"""
    type and enter to use
    e.g.
    lion
    tiger
"""
wordLst = []
def checkForSubstring(input_word, substring):
    return substring in input_word

#check same word
def checkSameWord(input, lst):
    if len(lst) > 1:
        for word in lst[:-1] :
            if checkForSubstring(input, word) or checkForSubstring(word, input):  
                return  (True,word)
    return False, None    

    
print("Start!! (Type exit to break)")
while (True):
    word = input()
    word.lower()

    #break condition and delete words in list
    if word == "exit" or word == "ออก":
        break
    if word == "del" or word == "ลบ":
        wordLst.remove(wordLst[-1])
        continue
    
    wordLst.append(word)
    checkSame, sameWord = checkSameWord(word,wordLst)
    #show same words
    if checkSame:
        print("Same word found!")
        print(f"Current word: {word}")
        print(f"Similar to: {sameWord}")
    
print("word list :", wordLst)
