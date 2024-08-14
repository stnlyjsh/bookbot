char_count = {}
dict_two = []

def main():
    get_text()
    count()
    chars()
    dict_two = convert(char_count)
    report(dict_two)
    
def get_text():
    with open("books/frankenstein.txt") as f:
        #print frankenstein to console
        file_contents = f.read()
        return file_contents
    
def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordlist = file_contents.split()
        numWords = len(wordlist)
        return numWords

def chars():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower = file_contents.lower()
        #char_count = {}
        for character in lower:
            if character.isalpha() and character in char_count:
                char_count[character] += 1
            elif character.isalpha():
                char_count[character] = 1
        return char_count

def convert(dict):
        dict_two = [{"char" : key, "num" : int(value)} for key,value in dict.items()]
        dict_two.sort(reverse=True, key=sort_on)
        return dict_two

def sort_on(dict):
    return dict["num"]

def report(dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print("%d words found in the document \n" % (count()))
    for pair in dict:
        print("The '%s' character was found '%i' times" % (pair["char"], pair["num"]))
    print("--- End report ---")    
main()