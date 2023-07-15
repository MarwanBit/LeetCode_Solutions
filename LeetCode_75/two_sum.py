class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Having trouble understanding how to handle hash collisions 
        '''
        hash_map = {}
        for i, num in enumerate(nums):
            #add this num to our hash map
            print(num)
            print(hash_map)
            if num not in hash_map:
                hash_map[num] = [i]
            elif num in hash_map:
                hash_map[num].append(i)
            print(num)
            print(hash_map)
            #now we check if target - num is in the index
            if (target - num) in hash_map and (target - num != num):
                return [hash_map[num][0], hash_map[target - num][0]]
            elif (target - num) in hash_map and (target - num == num) and len(hash_map[num]) > 1:
                return hash_map[num]
    

    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        '''
        O(n^2) time and O(1) space 
        '''
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3,2,4], 6))