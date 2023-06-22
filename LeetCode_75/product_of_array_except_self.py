class Solution:

    #This solution is to slow O(N^3) I think?? or N^2
    def productExceptSelfHelper(self, nums: list[int]) -> list[int]:
        '''
        '''
        index_set = {index for index in range(len(nums))}
        combos = []
        for index in index_set:
           combos.append(index_set - {index})
        return combos
    

    #O(N^2) is the set operation is constant time (which I think it is)
    #Way to slow we need to come up with a faster way, I know how to do this if the array is 
    # all non-zero and we can use division, it is really easy (multiply the array all together) and then divide by num[i]
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        '''
        combos = self.productExceptSelfHelper(nums)
        product_array = []
        for combo in combos:
            prod = 1 
            for index in combo:
                prod *= nums[index]
            product_array.append(prod)
        return product_array
    

    def productExceptSelfOptimal(self, nums: list[int]) -> list[int]:
        '''
        This way uses the prefix and postfix arrays as shown by NeetCode's Video
        '''
        prefix = []
        postfix = [0 for index in range(len(nums))]
        product_array = []
        #This will create the prefix array in O(n) time
        for index in range(len(nums)):
            if index == 0:
                prefix.append(nums[0])
            elif index >= 1:
                prefix.append(nums[index]*prefix[index - 1])
        #Now we create the postfix array in O(n) time
        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                postfix[len(nums) - 1] = nums[len(nums) - 1]
            else:
                postfix[index] = nums[index]* postfix[index + 1]
        #Now we loop through and the length of nums to create a product array
        print(prefix)
        print(postfix)
        for index in range(len(nums)):
            if index == 0:
                product_array.append(1*postfix[1])
            elif index != len(nums) - 1:
                product_array.append(prefix[index - 1]*postfix[index + 1])
            elif index == len(nums) - 1:
                product_array.append(prefix[index - 1]*1)
        
        return product_array



if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3 ,4]
    print(sol.productExceptSelfHelper(nums))
    print(sol.productExceptSelf(nums))
    print(sol.productExceptSelfOptimal(nums))