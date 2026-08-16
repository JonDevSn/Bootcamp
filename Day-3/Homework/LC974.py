class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        remainder_counts = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            rem = running_sum % k

            if rem in remainder_counts:
                count += remainder_counts[rem]
                remainder_counts[rem] += 1
            else:
                remainder_counts[rem] = 1

        return count