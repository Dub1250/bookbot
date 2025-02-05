# Author Ethan Ruark
# Boot.dev Guided Project: BookBot

def characterCount(file):
    charDict = {}
    for c in file:
        i = c.lower()
        if i == '\n':
            i = 'newline'
        if i == "":
            charDict[""] += 1
        elif i in charDict:
            charDict[i] += 1
        else:
            charDict[i] = 1
    return charDict


def wordCount(file):
    wordDict = {}
    words = file.split()
    for word in words:
        i = word.lower()
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1
    return (len(words), wordDict)


def main():    
    print("*" * 50)
    print("Welcome to the new and upgraded BookBot")
    print("*" * 50)
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#    for c in file_contents:
#        i = c.lower()#        
#        if i.isalpha():
#            if i in charDict:
#                charDict[i] += 1
#            else:
#                charDict[i] = 1
    wordCounts = wordCount(file_contents)
    charDict = characterCount(file_contents)

    print("--- Begin frankenstein.txt letter count ---")
    print(f"{wordCount} words found in the document\n\n")
    for c in charDict:
        print(f"The '{c}' character was found {charDict[c]} times")
    print("\n--- End Report ---\n")


if __name__ == "__main__":
    main()
