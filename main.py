# Author Ethan Ruark
# Boot.dev Guided Project: BookBot

def main():
    charDict = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
#       wordCount = len(words)

    for word in words:
        for i in word:
            p = i.lower()
            if p in charDict:
                charDict[p] += 1
            else:
                charDict[p] = 1

    print(charDict)


if __name__ == "__main__":
    main()
