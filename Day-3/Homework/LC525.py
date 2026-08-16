class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        sum_to_index = {0: -1}
        running_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in sum_to_index:
                max_len = max(max_len, i - sum_to_index[running_sum])
            else:
                sum_to_index[running_sum] = i

        return max_len