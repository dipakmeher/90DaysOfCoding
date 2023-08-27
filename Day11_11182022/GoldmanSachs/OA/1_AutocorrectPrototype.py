def getSearchResults(words, queries):
    sorted_words = [sorted(word) for word in words]
    result = []

    for q in queries:
        temp = []
        sorted_q = sorted(q)
        
        for idx, sorted_word in enumerate(sorted_words):
            if sorted_word == sorted_q:
                temp.append(words[idx])
        
        temp.sort()
        result.append(temp)

    return result

#Main
words = ["duel", "speed", "dule", "cars"]
# words = ["emits","items","baker","times","break"]
# queries = ["mites", "brake"]
queries = ["spede", "deul"]
print("Autocorrect prototype: ",getSearchResults(words,queries))


