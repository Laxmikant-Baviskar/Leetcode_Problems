
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_val = min(prices)
        # i = prices.index(min_val)
        # max_i = max(prices[i : ])

        # if prices[i] >= len(prices):
        #     return 0
        # else:
        #     return max_i - min_val

        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.



# Example 3: *******imp*******
# Input: prices = [2,4,1]
# Output: 2


# ==============================
# prices = [7,8,1,5,3,6,4]
# min_val = min(prices) 
# # low_index = prices.index(min_val
# i = prices.index(min_val)

# max_i = max(prices[i : ])

# print(max_i - min_val ) 

# =========================== # 
