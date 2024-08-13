def main():
    with open("books/frankenstein.txt") as f:
        #print frankenstein to console
        file_contents = f.read()
        return print(file_contents)
    
def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordlist = file_contents.split()
        numWords = len(wordlist)
        return print(numWords)

#main()
count()