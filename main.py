# Author Ethan Ruark
# Boot.dev Guided Project: BookBot

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = len(words)

    print(wordCount)
    

if __name__ == "__main__":
    main()