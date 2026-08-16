from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time Complexity: O(m + n)
        Space Complexity: O(k) where k is the number of unique characters in t
        """
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        window_counts = {}
        have, need = 0, len(target_counts)
        res = (-1, -1)
        min_len = float("inf")
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = (left, right)

                window_counts[s[left]] -= 1
                if s[left] in target_counts and window_counts[s[left]] < target_counts[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if min_len != float("inf") else ""