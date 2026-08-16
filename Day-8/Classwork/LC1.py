class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []