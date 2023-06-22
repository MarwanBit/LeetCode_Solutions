class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output_list = []
        max_candy = max(candies)
        for value in candies:
            if value + extraCandies >= max_candy:
                output_list.append(True)
            else:
                output_list.append(False)
        return output_list
    
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [c + extraCandies for c in candies]