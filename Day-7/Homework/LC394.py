class Solution(object):
    def decodeString(self, s):
        stack = []
        current = ""
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                stack.append((num, current))
                num = 0
                current = ""

            elif ch == "]":
                count, previous = stack.pop()
                current = previous + current * count

            else:
                current += ch

        return current