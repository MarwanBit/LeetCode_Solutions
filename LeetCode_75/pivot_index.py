class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        '''
        The approach here is to produce two arrays, left_sum and right_sum
        which calculate the sums of the number left and right of the current index,
        we can then iterate through out nums list and find which ones satisfy left_sum[i] == right_sum[i]

        This will be O(N) time complexity and O(N) storage because we store 2 size N lists
        '''
        left_sums: list[int] = [0]*len(nums)
        right_sums: list[int] = [0]*len(nums)
        left_sums[0] = 0
        right_sums[len(nums) - 1] = 0
        # now we construct our left_sums list
        for index in range(1, len(nums)):
            left_sums[index] = nums[index - 1] + left_sums[index - 1]
        # now we construct our right_sums list
        for index in range(len(nums) - 2, -1, -1):
            right_sums[index] = nums[index + 1] + right_sums[index + 1]
        #Now we iterate through and see if we get a right solution
        for index in range(len(nums)):
            if left_sums[index] == right_sums[index]:
                return index
        return -1

    def pivotIndexOpt(self, nums: list[int]) -> int:
        '''
        The approach above works well in the sense that we have O(N) time complexity and O(N) storage, but this 
        is not as efficient as we could have, we want to see if we can make this more efficient with the goal of making it
        O(N) time complexity and O(1) storage, lets try to figure out how we can do this 
        '''
        s = sum(nums)
        left_sum = 0 
        for index in range(len(nums)):
            x_i = nums[index]
            if (s - left_sum - x_i) == (left_sum):
                return index
            left_sum += x_i
        return - 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.pivotIndex([1,7,3,6,5,6]))
    print(sol.pivotIndex([1,2,3]))
    print(sol.pivotIndex([2, 1, -1]))
    print(sol.pivotIndexOpt([1,7,3,6,5,6]))
    print(sol.pivotIndexOpt([1,2,3]))
    print(sol.pivotIndexOpt([2, 1, -1]))