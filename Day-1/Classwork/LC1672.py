class Solution(object):
    def maximumWealth(self, accounts):
        maxw = 0
        for customer in accounts:
            wealth = sum(customer)
            maxw = max(maxw, wealth)

        return maxw
        