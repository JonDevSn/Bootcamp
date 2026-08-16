class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(min(n, k))
        """
        remainder_map = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            rem = running_sum % k

            if rem in remainder_map:
                if i - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = i

        return False