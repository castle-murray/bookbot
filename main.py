from pathlib import Path

character_count = {}
bookpath = Path("books")
frankenstein = bookpath / "frankenstein.txt"
with frankenstein.open() as f:
    file_contents = f.read()
    # count words in file_contents
    file_contents = file_contents.lower()
    words = file_contents.split()
    count = len(words)
    characters = list(file_contents)
    for character in characters:
        if character in character_count and character.isalpha():
            character_count[character] += 1
        elif character.isalpha():
            character_count[character] = 1

    

print("---begin report of books/frankenstein.txt---")
print(f"{count} words found in the document\n")
for character, count in character_count.items():
    print(f"the '{character}' character was fonud {count} times")

