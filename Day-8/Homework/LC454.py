from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        count = 0
        sum_ab = defaultdict(int)

        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1

        for c in nums3:
            for d in nums4:
                count += sum_ab[-(c + d)]

        return count