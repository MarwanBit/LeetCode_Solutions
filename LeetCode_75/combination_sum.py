class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        combinations = set()
        def backtrack(k, n, currList):
            if k < 0 and n < 0:
                return 
            elif k == 0 and n == 0:
                combinations.add(frozenset(currList))
            elif k == 0 and n != 0:
                return
            else:
                for digit in range(1, 10):
                    if digit not in currList:
                        temp = currList + [digit]
                        backtrack(k - 1, n - digit, temp)
        
        backtrack(k, n, [])
        return combinations