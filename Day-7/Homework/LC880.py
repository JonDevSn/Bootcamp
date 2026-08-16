class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        size = 0

        # Calculate the total decoded size
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        # Work backwards to find the k-th character
        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                size //= int(char)
            else:
                size -= 1

        return ""