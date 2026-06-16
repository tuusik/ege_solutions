class Solution:
    def maximumWealth(self, accounts):
        res = 0
        for i in range(len(accounts)):
            temp = sum(accounts[i])
            if temp > res:
                res = temp
        return res