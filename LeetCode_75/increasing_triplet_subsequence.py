class Solution:
    #O(N^3) solution :( (To Slow but works!)
    def increasingTriplet(self, nums: list[int]) -> bool:
        '''
        '''
        i = 0
        j = 0 
        k = 0 
        while (i != len(nums) - 1):
            while (j != len(nums) - 1):
                #finds first possible j index
                while (nums[j] <= nums[i]) and (j != len(nums) - 1):
                    j += 1
                    k += 1
                #finds first possible k index after the given j index
                while (nums[k] <= nums[j]) and (k != len(nums) - 1):
                    k += 1
                #Now check if it is a valid sequence 
                if (i < j < k) and (nums[i] < nums[j] < nums[k]):
                    return True 
                # if we can iterate j we do so an try again
                if (j <= len(nums) - 2):
                    j += 1
                    k = j
            #if we can iterate i we do so and try again
            if (i <= len(nums) - 2):
                i += 1 
                j = i 
                k = i
        #other wise return false
        return False
    
    def increasingTripletOptimal(self, nums: list[int]) -> int:
        '''
        '''
        #Easy Base case
        if len(nums) < 3:
            return False
        left_min_list = [0]*len(nums)
        right_max_list = [0]*len(nums)
        #first we must create the right min list
        left_min_list[0] = nums[0]
        for index in range(1, len(nums)):
            left_min_list[index] = min(nums[index], left_min_list[index - 1])
        #now we create the left max list
        right_max_list[len(nums) - 1] = nums[len(nums) - 1]
        for index in range(len(nums) - 2, -1, -1):
            right_max_list[index] = max(nums[index], right_max_list[index + 1])
        #now we loop through the nums list and check if a pair exists
        for index in range(len(nums)):
            if (left_min_list[index] < nums[index]) and (nums[index] < right_max_list[index]):
                return True
        return False
    

    
if __name__ == "__main__":
    sol = Solution()
    nums = [20,100,10,12,5,13]
    print(sol.increasingTriplet(nums))