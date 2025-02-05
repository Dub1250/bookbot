# Author Ethan Ruark
# Boot.dev Guided Project: BookBot

def characterCount(file, fileName):
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

    print(f"\n--- Begin {fileName} letter count ---\n")
    for c in charDict:
        print(f"The '{c}' character was found {charDict[c]} times")
    print("\n--- End Report ---\n")


def wordCount(file, fileName):
    wordDict = {}
    words = file.split()
    for word in words:
        i = word.lower()
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1

    print(f"\n--- Begin {fileName} letter count ---\n")
    print(f"{len(words)} words found in the document\n")
    for c in wordDict:
        print(f"The word '{c}' was found {wordDict[c]} times")
    print("\n--- End Report ---\n")


def main():    
    print("*" * 50)
    print("   ", "Welcome to the new and improved BookBot")
    print("*" * 50)

    source = input("\nPlease insert the file path of the"
                   " text you wish to analyze: ")
    fileName = input("file name?: ")

    with open(source) as src:
        file_contents = src.read()

    print("Please select an option: \n"
          "1. word count\n"
          "2. character count\n")
    option = input("Option #: ")
    if option == "1":
        wordCount(file_contents, fileName)
    elif option == "2":
        characterCount(file_contents, fileName)
#    
# for c in file_contents:
#        i = c.lower()#        
#        if i.isalpha():
#            if i in charDict:
#                charDict[i] += 1
#            else:
#                charDict[i] = 1


if __name__ == "__main__":
    main()
