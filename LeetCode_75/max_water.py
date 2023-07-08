class Solution:
    def maxAreaAttempt(self, height: list[int]) -> int:
            '''
            Notice that given two indices i and j such that
            WLOG i < j we have that A(i,j) = min(height[i], height[j])*(j-i)

            One thing we can do to solve this is iterate through the entire
            array to get pairs of indices to try and try all of them from there.

            This approach would be O(N^2) which is not good.

            Here are my ideas for optimization:
                - Greedy approach of trying argmax h[i] and finding the index where
                                                i
                    it occurs and try everything before and after it.
                - Notice that the Area is always constrained by the min(i, j) so looking
                for to maximize this is a goal.
                - The problem with this approach is the (j - i) term, we need some control
                over it in order to be sure we'll have an algorithm which gets 
                the right anwser.
                - Let's play around with some examples to find out how to approach this

            Big Notice:
                -Notice that because the heights are integers, aslong as we increase
                the min height we don't have to even worry about the (j - i) term since 
                it'll cancel out

            #DP???
            '''
            #Declare variables for the two pointers
            max_vol = 0
            i = 0 
            j = len(height) - 1
            #when we can still upgrade to do better
            while ((height[i] < height[i + 1]) or (height[j] < height[j-1])) and (i != j) and (j - 1 != i) and (i + 1 != j):
                print("i: " + str(i) + "and j: " + str(j))
                min_height = min(height[i], height[j])
                if (height[i] < height[i + 1]) and (min_height == height[i]) and (i + 1 != j):
                    i += 1 
                    print("i: " + str(i) + "and j: " + str(j))
                if (height[j] < height[j - 1]) and (min_height == height[j]) and (j - 1 != i):
                    j -= 1
                    print("i: " + str(i) + "and j: " + str(j))
            return min(height[i], height[j])*(j-i)
            
    def maxArea(self, height: list[int]) -> int:
        '''
        '''
        #Declare variables for the two pointers
        max_vol = 0
        i = 0 
        j = len(height) - 1
        while i < j:
            max_vol = max(max_vol, (j - i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1 
        return max_vol

if __name__ == "__main__":
     sol = Solution()
     height = [1, 2, 1]
     print(sol.maxArea(height))