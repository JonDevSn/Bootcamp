class Solution(object):
    def calPoints(self, op):
        ans = []

        for i in range(len(op)):
            if op[i] == 'C':
                ans.pop()

            elif op[i] == 'D':
                ans.append(2 * ans[-1])

            elif op[i] == '+':
                ans.append(ans[-1] + ans[-2])

            else:
                ans.append(int(op[i]))

        return sum(ans)