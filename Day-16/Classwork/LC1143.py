class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for char1 in text1:
            prev = 0
            for j, char2 in enumerate(text2):
                temp = dp[j + 1]
                if char1 == char2:
                    dp[j + 1] = prev + 1
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                prev = temp

        return dp[-1]