class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = 0

        curr_max = 0
        max_sum = float('-inf')

        curr_min = 0
        min_sum = float('inf')

        for num in nums:
            total += num

            # Kadane for maximum subarray
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            # Kadane for minimum subarray
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        # All elements are negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)