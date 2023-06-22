class Solution:
    #Wrong solution, come back to it later
    def placeFlowersHelper(self, flowerbed: list[int]):
        '''
        '''
        count = 0

        #Handles the base case
        if len(flowerbed) == 1 or len(flowerbed) == 0:
            if flowerbed == [0]:
                count += 1
            else:
                #do nothing
                pass
        
        #Now we handle the case when len(flowerbed) >= 2
        elif len(flowerbed) >= 2:
            #split into even and odd cases
            if len(flowerbed) % 2 == 1:
                mid_flwr_idx = len(flowerbed) // 2
                mid_flwr = flowerbed[mid_flwr_idx]
                if (mid_flwr == 0 and flowerbed[mid_flwr_idx - 1] == 0 and flowerbed[mid_flwr_idx + 1] == 0):
                    count += 1
                    left_bed = self.placeFlowersHelper(flowerbed[0: mid_flwr_idx - 1])
                    right_bed = self.placeFlowersHelper(flowerbed[mid_flwr_idx + 2:])
                    count += left_bed + right_bed
                else:
                    left_bed = self.placeFlowersHelper(flowerbed[0: mid_flwr_idx])
                    right_bed = self.placeFlowersHelper(flowerbed[mid_flwr_idx + 1:])
                    count += left_bed + right_bed

            elif len(flowerbed) % 2 == 0:
                mid_flwr_idx = len(flowerbed) // 2
                left_bed = self.placeFlowersHelper(flowerbed[0: mid_flwr_idx])
                right_bed = self.placeFlowersHelper(flowerbed[mid_flwr_idx:])
                count += left_bed + right_bed
        
        return count




    
    def canPlaceFlowers(self, flowerbed: list[int], n:int) -> bool:
        '''
        '''
        count = self.placeFlowersHelper(flowerbed)
        return count >= n


    def canPlaceFlowersCorrect(self, flowerbed: list[int], n:int) -> bool:
        '''
        '''
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for index in range(1, len(flowerbed) - 1):
            if (flowerbed[index - 1] == 0) and (flowerbed[index] == 0) and (flowerbed[index + 1] == 0):
                count += 1 
                flowerbed[index] = 1
        
        return count >= n

if __name__ == "__main__":
    Sol = Solution()
    flowerbed = [1,0,0,0,1]
    print(Sol.canPlaceFlowers(flowerbed, 1))
    print(Sol.canPlaceFlowers(flowerbed, 2))

    flowerbed = [1,1,0,0,0,0,0]
    print(Sol.canPlaceFlowers(flowerbed, 2))




