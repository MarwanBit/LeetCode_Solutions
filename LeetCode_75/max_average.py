class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        '''

        Now the idea is to create some lists called left_sum and right_sum
        which will take O(N) time complexity each and we will use this to calculate
        the average at each instance
        '''

        #This is O(N^2) complexity :()
        # This is not fast enough so I expect that we must do something
        # regarding calculating the entire sum first
        total = sum(nums)
        max_average = -4000000
        left_sums = [0]*len(nums)
        right_sums = [0]*len(nums)
        i = 0 
        left_sums[0] = nums[0]
        right_sums[len(nums) - 1] = nums[len(nums) - 1]
        #Now let's generate our arrays
        for index in range(1, len(nums)):
            left_sums[index] = nums[index] + left_sums[index - 1]
        #Now let's generate the same array for the right sums
        for index in range(len(nums) - 2, -1, -1):
            right_sums[index] = nums[index] + right_sums[index + 1]

        print(left_sums)
        print(right_sums)

        print(i, k)
        while i + k  < len(nums):
            average = max_average
            print(i, i + k)
            print(average)
            if k == 1:
                print("k = 1 case")
                average = nums[i]
            else:
                print("other case")
                average =  (total - left_sums[i] - right_sums[i + k] + nums[i]) / k
            print(average)
            if average > max_average:
                print("new average")
                max_average = average
            i += 1
        return max_average
    
    def maxAverageOptimal(self, nums: list[int], k: int) -> float:
        '''
        '''
        sums = [0]*len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]
        res = sums[k - 1] / k
        for i in range(k, len(nums)):
            res = max(res, (sums[i] - sums[i - k]) / k)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    sol.findMaxAverage(nums, k)