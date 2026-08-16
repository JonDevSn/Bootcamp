#solve Leetcode problem 49: Group Anagrams
def groupAnagrams(strs):
    anagram_groups = {}
    for s in strs:
        # Sort the characters in the string to create a key
        sorted_str = ''.join(sorted(s))
        # Add the string to the appropriate group
        if sorted_str not in anagram_groups:
            anagram_groups[sorted_str] = []
        anagram_groups[sorted_str].append(s)
    # Return all the groups as a list of lists
    return list(anagram_groups.values())
