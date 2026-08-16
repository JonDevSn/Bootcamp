class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def at_most(goal: int) -> int:
            res = 0
            left = 0
            odd_count = 0

            for right in range(len(nums)):
                odd_count += nums[right] % 2
                while odd_count > goal:
                    odd_count -= nums[left] % 2
                    left += 1
                res += right - left + 1

            return res

        return at_most(k) - at_most(k - 1)