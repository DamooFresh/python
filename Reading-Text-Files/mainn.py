# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from cgitb import text


def read_file_content(filename):
    #[assignment] Add your code here 
    with open ('Reading-Text-Files\story.txt', 'r') as f:
        filena = f.read()
    
    return(filena)

print(read_file_content('Reading-Text-Files\story.txt'))


def count_words(text):
    text = read_file_content("Reading-Text-Files\story.txt")
    # [assignment] Add your code here
    counts = dict()
    dallo = text.lower().split()

    for word in dallo:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts    
    

print(count_words(text))


