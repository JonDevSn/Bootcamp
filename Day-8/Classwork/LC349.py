class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        return list(set(nums1) & set(nums2))