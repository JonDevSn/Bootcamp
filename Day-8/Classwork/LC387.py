from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1) - at most 26 lowercase English letters
        """
        count = Counter(s)

        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1