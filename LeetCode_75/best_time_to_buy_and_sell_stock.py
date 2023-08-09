class Solution:
    def maxProfitHelper(self, 
                        time_index: int, has_stock: bool, 
                        current_cost: int, prices: list[int],
                        fee: int
                        ) -> int:
        #Base cases
        if time_index > len(prices) - 1:
            return current_cost
        #if we have no stock currently we have two options, we can buy a stock
        # or we can move on 
        #We can choose not to buy 
        no_buy_branch = self.maxProfitHelper(
            time_index + 1, has_stock, 
            current_cost, prices,
            fee
        )
        if not has_stock:
            #we can buy 
            buy_cost = current_cost - (prices[time_index] + fee)
            buy_branch = self.maxProfitHelper(
                time_index + 1, True, 
                buy_cost, prices, 
                fee
                )
            return max(buy_branch, no_buy_branch)
        else:
            sell_cost = current_cost + prices[time_index]
            sell_branch = self.maxProfitHelper(
                time_index + 1, False, 
                sell_cost, prices,
                fee
            )
            #we can choose to sell or move on
            return max(sell_branch, no_buy_branch)
    def maxProfit(self, prices: list[int], fee: int) -> int:
        return self.maxProfitHelper(
            0, False, 
            0, prices,
            fee
        )