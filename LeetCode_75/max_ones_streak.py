class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        '''
        '''
        ones_streak: int = 0
        streak_list: list[int] = [0]*len(nums)
        streak_list[0] = int(nums[0])
        #Now we iterate through our streak_list and construct it
        for index in range(1, len(streak_list)):
            if nums[index] == 1:
                streak_list[index] = 1 + streak_list[index - 1]
            elif nums[index] == 0:
                streak_list[index] = 0 
        #now we create our sliding window
        for index in range(len(nums)):
            current_streak = 0 
            k_counter = k
            wndw_offset = 0
            # keep incrementing the sliding window until we cannot
            # increase the window size
            while (index + wndw_offset < len(nums) - 1) and (k_counter > 0):
                #if the current item is a 1 increment the streak
                if nums[index + wndw_offset] == 1:
                    current_streak += 1 
                    wndw_offset += 1
                elif nums[index + wndw_offset] == 0 and k_counter > 0:
                    current_streak += 1
                    wndw_offset += 1 
                    k_counter -= 1
            #after the end of this process we check if current_streak > ones_streak
            ones_streak = max(current_streak, ones_streak)
            index += 1
        return ones_streak
    
    def longestOnesOpt(self, nums: list[int], k: int) -> int:
        '''
        '''
        i: int = 0 
        j: int = 0 
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1 
            j += 1
        return j - i
    

if __name__ == "__main__":
    sol = Solution()
