# This approach checks if each character in string s maps to a unique character in string t.  
# It uses a dictionary to track character mappings and a set to ensure no duplicate values in t.  
# If a character in s is already mapped, it must map to the same character in t; otherwise, the strings aren't isomorphic.

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}  # To store mapping from characters in s to t
    mapped = set()  # To store already mapped characters in t

    for c1, c2 in zip(s, t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False  # Mapping mismatch
        else:
            if c2 in mapped:
                return False  # Character already mapped to another one
            s_to_t[c1] = c2
            mapped.add(c2)

    return True

# Example usage
print(isIsomorphic("egg", "add"))    # True
print(isIsomorphic("foo", "bar"))    # False
print(isIsomorphic("paper", "title"))  # True
