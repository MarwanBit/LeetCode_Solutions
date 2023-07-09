class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        '''
        '''
        max_altitude = 0
        current_alt = 0 
        for index in range(len(gain)):
            current_alt = current_alt + gain[index]
            max_altitude = max(max_altitude, current_alt)
        return max_altitude
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestAltitude([-5,1,5,0,-7]))
    print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))