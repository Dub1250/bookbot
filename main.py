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
    print("   ", "Welcome to the new and improved BookBot")
    print("*" * 50)
    
    source = input("\nPlease insert the file path of the text you wish to analyze: ")
    
    with open(source) as src:
        file_contents = src.read()
#    for c in file_contents:
#        i = c.lower()#        
#        if i.isalpha():
#            if i in charDict:
#                charDict[i] += 1
#            else:
#                charDict[i] = 1
    wordCounts = wordCount(file_contents)
    charDict = characterCount(file_contents)

    print("\n--- Begin frankenstein.txt letter count ---\n")
    print(f"{wordCounts[0]} words found in the document\n")
    for c in charDict:
        print(f"The '{c}' character was found {charDict[c]} times")
    print("\n--- End Report ---\n")


if __name__ == "__main__":
    main()
