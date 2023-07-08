class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        '''
        '''
        num_zeros = 0 
        max_length = 0
        left: int = 0 
        right: int = 0

        if nums == [1]*len(nums):
            print(len(nums) - 1)
            return len(nums) - 1

        while right < len(nums):
            print(left, right)
            if nums[right] == 1:
                right += 1
            elif nums[right] == 0 and num_zeros == 0:
                right += 1
                num_zeros += 1
            elif nums[right] == 0 and num_zeros == 1:
                if nums[left] == 0:
                    left += 1
                    num_zeros -= 1
                elif nums[left] == 1:
                    left += 1
            max_length = max((right - left) - num_zeros, max_length)
        print(max_length)
        return max_length
    

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,0,1]
    sol.longestSubarray(nums)
    print("Next Problem")
    sol.longestSubarray([0,1,1,1,0,1,1,0,1])
    print("Next Problem")
    sol.longestSubarray([1,1,1])