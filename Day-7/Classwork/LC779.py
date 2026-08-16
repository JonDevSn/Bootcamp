class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return (k - 1).bit_count() & 1