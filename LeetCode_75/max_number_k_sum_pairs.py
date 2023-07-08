import math

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        '''
        O(nlogn) time complexity with O(1) space complexity sol

        the idea is to sort through the array and then use a left 
        and right pointer to find a pair, if we find a pair we increment
        the pointers and continue
        '''
        i, j = 0, len(nums) - 1
        count = 0
        nums.sort()
        while (i < j):
            pair_sum = nums[i] + nums[j]
            if pair_sum == k:
                i += 1
                j -= 1 
                count += 1
            elif pair_sum > k:
                j -= 1
            else:
                i += 1
        return count
    
    def maxOperationsHashTable(self, nums: list[int], k: int) -> int:
        '''
        The idea is to take advantage of the fact that we have the number of pairs 
        that sum to k in  a list is min(count(x), count(k - x)) unless x = k/2 than
        is if floor(count(x)/2)

        So what we do is create a hashmap that maps value_in_nums --> number of occurences
        we can create this hashmap in O(n) time
        '''
        count = 0
        hash_map = {}
        for value in nums:
            if value not in hash_map.keys():
                hash_map[value] = 1 
            else:
                hash_map[value] += 1
        #now we iterate through the values in the hash_map
        for x in hash_map.keys():
            # first check if x != k / 2
            if x != k / 2:
                if (k - x) in hash_map:
                    count += min(hash_map[x], hash_map[k - x])
                    hash_map[x] = 0 
                    hash_map [k - x] = 0
            else:
                count += math.floor(hash_map[x] /  2)
        return count 