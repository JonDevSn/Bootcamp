from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time Complexity: O(m + n) where m = len(s), n = len(t)
        Space Complexity: O(m + n) (or O(1) bounded by character set size)
        """
        if not s or not t:
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts = defaultdict(int)
        formed = 0

        left = 0
        min_len = float("inf")
        best_window = (0, 0)

        for right, char in enumerate(s):
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_window = (left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float("inf") else s[best_window[0] : best_window[1] + 1]