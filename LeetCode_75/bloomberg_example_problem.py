import math

class Solution:
    #take two lists L1 and L2 of numbers and return the unique pair which 
    # has the smallest distance
    def minDistance(self, list1: str, list2: str) -> float:
        #First let's combine the lists 
        # let's label the lists 
        min_distance = 2*max(max(list1), max(list2))
        list1 = list(map(lambda x: (x, "a"), list1))
        list2 = list(map(lambda x: (x, "b"), list2))
        #now let's combine the lists 
        combo_list = list1 + list2
        #now we want to sort 
        combo_list = sorted(combo_list, key = lambda x: x[0])
        #now let's create two points 
        left = 0 
        right = 0 
        while left < len(combo_list) - 1:
            #Move right till match 
            left_val, left_label = combo_list[left]
            right_val, right_label = combo_list[right]
            distance = math.fabs(left_val - right_val)
            not_match = not (left_label != right_label and distance != 0)
            while not_match and right < len(combo_list) - 1:
                right += 1
                right_val, right_label = combo_list[right]
                distance = math.fabs(left_val - right_val)
                not_match = not(left_label != right_label and distance != 0)  
            #now we can assume we have a match 
            if not not_match:
                min_distance = min(min_distance, distance)
            #now we move the left pointer to the left 
            while left < right: 
                left += 1 
                left_val, left_label = combo_list[left]
                match = (left_label != right_label) and (distance != 0)
                if match:
                    min_distance = min(min_distance, distance)
            # This should take care of it??
        return min_distance 
                        

                    
        

if __name__ == "__main__":
    solution = Solution()
    list1 = [1]
    list2 = [1,2,3]

    print(solution.minDistance(list1, list2))

    list1 = [2, 26]
    list2 = [7, 4, 80]

    print(solution.minDistance(list1, list2))

    list1 = [5,7,11]
    list2 = [3]

    print(solution.minDistance(list1, list2))