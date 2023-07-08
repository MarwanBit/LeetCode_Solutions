class Solution:
    def maxCandies(self, candies: list[int], extraCandies: int) -> list[int]:
        '''
        '''
        max_candies = max(candies)
        for index, candy_count in enumerate(candies):
            if candy_count +  extraCandies >= max_candies:
                candies[index] = True
            else:
                candies[index] = False
        return candies

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extra_candies = 3
    sol = Solution()
    print(sol.maxCandies(candies, extra_candies))