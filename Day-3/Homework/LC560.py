class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        prefix_counts = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            diff = running_sum - k

            if diff in prefix_counts:
                count += prefix_counts[diff]

            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1

        return count