class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        max_len = 0
        count = 0
        seen = {0: -1}

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in seen:
                max_len = max(max_len, i - seen[count])
            else:
                seen[count] = i

        return max_len