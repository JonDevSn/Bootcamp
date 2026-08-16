class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Time Complexity: O(n * L) where n is len(s) and L is max length of a word in wordDict
        Space Complexity: O(n + k) where k is the space for the word set
        """
        word_set = set(wordDict)
        max_len = max(len(w) for w in word_set)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]