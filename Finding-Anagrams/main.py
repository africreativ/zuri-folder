# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = sorted(word)
    anagram = sorted(anagram)
    if len(word) != len(anagram):
        return False
    elif word == anagram:
        return True
    else:
        return False



check = find_anagram("below", "elbow")
print(check)
