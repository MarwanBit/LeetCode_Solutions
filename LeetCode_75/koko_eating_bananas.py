import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            hours = 0 
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11], 8))
