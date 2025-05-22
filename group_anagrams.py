
# This approach uses prime number multiplication to uniquely identify anagram groups.  
# Each letter maps to a prime; product of primes for a word is the same for all its anagrams.  
# We group words by this prime product using a dictionary.

from collections import defaultdict

def groupAnagrams(words):
    # Map each letter a-z to a unique prime number
    prime_map = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    ]
    
    anagram_groups = defaultdict(list)

    for word in words:
        product = 1
        for char in word:
            product *= prime_map[ord(char) - ord('a')]
        anagram_groups[product].append(word)

    return list(anagram_groups.values())

# Example usage
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_words))

