class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit) #only changes if "profit" is higher than "maxprofit"
            else:
                l=r #if right is lower, left needs to move to the lowest point
            r+=1
        return maxprofit