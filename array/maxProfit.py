def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_profit = 0

        for curr in prices:
            if buy > curr:
                buy = curr

            curr_profit = curr - buy
            if curr_profit > max_profit :
                max_profit = curr_profit
        return max_profit
