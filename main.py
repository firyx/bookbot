path = "books/frankenstein.txt"

def main():
    file_content = read_file(path)
    word_count = count_words(file_content)
    char_freq = count_chars_freq(file_content)
    letter_freq_sorted = sort_letters(char_freq)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter_freq in letter_freq_sorted:
        print(f"The '{letter_freq['letter']}' character was found {letter_freq['count']} times")
    print("--- End report ---")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    return len(str.split())

def count_chars_freq(str):
    lower = str.lower()
    char_freq = {}
    for char in lower:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def sort_letters(char_freq):
    letters_sorted = []
    for char in char_freq:
        if char.isalpha():
            letters_sorted.append({"letter": char, "count": char_freq[char]})
    letters_sorted.sort(reverse=True, key=lambda e: e["count"])
    return letters_sorted

main()
