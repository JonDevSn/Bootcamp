from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        freq = defaultdict(int)
        current_sum = 0
        max_sum = 0

        # Initialize the first window of size k
        for i in range(k):
            freq[nums[i]] += 1
            current_sum += nums[i]

        if len(freq) == k:
            max_sum = current_sum

        # Slide the window across the array
        for i in range(k, len(nums)):
            # Add incoming element
            freq[nums[i]] += 1
            current_sum += nums[i]

            # Remove outgoing element
            out = nums[i - k]
            current_sum -= out
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]

            # Update max_sum if all elements in the window are distinct
            if len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum