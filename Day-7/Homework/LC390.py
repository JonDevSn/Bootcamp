class Solution(object):
    def lastRemaining(self, n):
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:

            # Head changes if eliminating from left
            # OR if number of elements is odd
            if left or remaining % 2 == 1:
                head += step

            # Half the elements are removed
            remaining //= 2

            # Distance between elements doubles
            step *= 2

            # Change direction
            left = not left

        return head