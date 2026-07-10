class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in accounts:
            total = 0
            for money in i:
                total += money
                if total > richest:
                    richest = total
        return richest
            