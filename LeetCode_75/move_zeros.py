class Solution:
    def moveZeroesOptimal(self, nums: list[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.

            O(n) time, O(n) memory
            """
            num_zeros = 0
            ans = []
            for num in nums:
                if (num == 0):
                    num_zeros += 1
            #now we iterate through the solution
            for index in range(len(nums)):
                if nums[index] != 0:
                    ans.append(nums[index])
            # now we go back and add the nums
            for zero_count in range(num_zeros):
                ans.append(0)
            print(num_zeros)
            print(ans)
            print(nums)
            # finally we go through and modify nums
            for index in range(len(nums)):
                nums[index] = ans[index]
            return nums
    
    def moveZeros(self, nums: list[int]) -> None:
        '''
        I think this approach is O(n^2) time, O(1) memory
        '''
        i, j, k = 0, 0, 0
        while (i != len(nums) - 1):
            #now we check that i isn't pointing to a zero
            while (nums[i] != 0 and i != len(nums) - 1):
                i += 1
                j += 1
            # now we should be pointing to a 0 ideally, so we iterate j
            while (nums[j] == 0 and j != len(nums) - 1):
                j += 1
            #now what we should have is a pair where i points to a 0
            # and j points to a non-zero element, now we swap them
            nums[i], nums[j] = nums[j], nums[i]
            k += 1 
            i,j = k, k
        return nums
    

    def moveZeroesOptimal2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        #This solution is O(n) time and O(1) space
        """
        last_non_zero = 0
        #this loop pushes all the non-zero elements to the front in order
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[last_non_zero] = nums[index]
                last_non_zero += 1 
        for index in range(last_non_zero, len(nums)):
            nums[index] = 0
        return nums
        


if __name__ == "__main__":
     sol = Solution()
     nums_list = [0, 1, 0, 3, 12]
     print(sol.moveZeroes(nums_list))