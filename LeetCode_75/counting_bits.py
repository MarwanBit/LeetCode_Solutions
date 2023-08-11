from functools import reduce

class Solution:
    def countBits(self, n: int) -> list[int]:
        '''
        Here's the pattern I notice:
        
        in the first section: 0 | 1   length = 2
        second section : 1 | 2        length = 2
        third section: 1, 2 | 2, 3    length = 4
        fourth section: 1, 2, 2, 3 | 2, 3, 3, 4  length = 8

        guess for fifth section:  length = 16 so
        1, 2, 2, 3, 2, 3, 3 , 4 | 2, 3, 3, 4, 3, 4, 4, 5

        The nth section is equal to (n - 1 th section) | (n- 1th section) + 1 (element wise)

        The idea for the algorithm is to create each of these sections
        by first taking N and finding the number of sections, i.e we want 
        
        k s.t.

        2^k >= n 

        we use this to create a list of sections, which we 
        '''
        #first lets deal with base cases 
        if n == 0:
            return [0]
        if n == 1: 
            return [0, 1]
        sections_num = 1
        k = 1 
        while k < n:
            k = 2*k 
            sections_num += 1 
        dp = [[] for _ in range(sections_num)]
        dp[0] = [0, 1]
        dp[1] = [1, 2]
        for i in range(2, sections_num):
            dp[i] = dp[i - 1] + [1 + x for x in dp[i - 1]]
        res = reduce(lambda x, y: x + y, dp)
        return res[:n + 1]