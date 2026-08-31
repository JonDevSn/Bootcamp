class Solution(object):
    def removeDuplicates(self, s):
        ans = []

        for i in range(len(s)):
            if ans and s[i] == ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])

        return "".join(ans)