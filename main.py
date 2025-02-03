# Author Ethan Ruark
# Boot.dev Guided Project: BookBot

def main():
    charDict = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = len(words)

    for c in file_contents:
        i = c.lower()
#        if i == "":
#            charDict[""] += 1
#        elif i in charDict:
#            charDict[i] += 1
#        else:
#            charDict[i] = 1
        if i.isalpha():
            if i in charDict:
                charDict[i] += 1
            else:
                charDict[i] = 1

    print("--- Begin frankenstein.txt letter count ---")
    print(f"{wordCount} words found in the document\n\n")
    for c in charDict:
        print(f"The '{c}' character was found {charDict[c]} times")
    print("\n--- End Report ---\n")


if __name__ == "__main__":
    main()
