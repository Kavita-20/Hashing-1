#Split the input string into words and check if its length matches the pattern's length.
#Use two hash maps to maintain a bijection between each character in the pattern and each word in the string.
#Ensure consistency in both mappings — no character maps to multiple words and vice versa.


def wordPattern(pattern: str, s: str) -> bool:
    # Split input string into words
    words = s.split()

    # Length mismatch means pattern can't match
    if len(pattern) != len(words):
        return False

    # Dictionaries to store mappings between pattern and words
    char_to_word = {}
    word_to_char = {}

    # Iterate through pattern and words together
    for ch, word in zip(pattern, words):
        if ch in char_to_word:
            # Existing mapping doesn't match current word
            if char_to_word[ch] != word:
                return False
        else:
            # Word already mapped to a different pattern character
            if word in word_to_char:
                return False
            # Add new mapping
            char_to_word[ch] = word
            word_to_char[word] = ch

    return True
