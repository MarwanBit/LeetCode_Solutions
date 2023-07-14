class Solution:
    def removeStars(self, s: str) -> str:
        '''
        This solution is O(N^2)
        but the space complexity is O(1) extra
        Not fast enough for leetcode :(
        '''
        left = len(s) - 1 
        right = len(s) - 1 
        s = list(s)
        while "*" in s:
            while s[right] != "*":
                right -= 1 
                left -= 1 
            while (s[left] == "*" or s[left] == "") and left > 0:
                left -= 1 
            s[left] = ""
            s[right] = ""
            left = right
        return "".join(s)
    
    def removeStarsOpt(self, s: str) -> str:
        '''
        Think this solution is O(N) in time 
        and O(N) in extra storage
        '''
        output_str = ""
        st = []
        for i in range(len(s)):
            if s[i] == "*":
                st.pop()
            else:
                st.append(s[i])
        for i in range(len(st)):
            output_str += st[i]
        return output_str
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeStars("erase*****"))
    print(sol.removeStars("abb*cdfg*****x*"))