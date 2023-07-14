class Solution:

    def getRow(self, grid:List[List[int]], row_number) -> List[int]:
        '''
        '''
        row = [0]*len(grid)
        for index in range(len(grid)):
            row[index] = grid[index][row_number]
        return row


    def getColumn(self, grid: List[List[int]], column_number) -> List[int]:
        '''
        '''
        column = [0]*len(grid)
        for index in range(len(grid)):
            column[index] = grid[column_number][index]
        return column
        

    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        '''
        number_pairs = 0
        for row_number in range(len(grid)):
            for column_number in range(len(grid)): 
                row = self.getRow(grid, row_number)
                column = self.getColumn(grid, column_number)
                if row == column:
                    number_pairs += 1 
        return number_pairs
    

    def equalPairsOpt(self, grid: List[List[int]]) -> int:
        '''
        '''
        number_pairs = 0
        for row_number in range(len(grid)):
            for column_number in range(len(grid)): 
                match = True
                for index in range(len(grid)):
                    if grid[index][row_number] != grid[column_number][index]:
                        match = False
                if match: 
                    number_pairs += 1 
        return number_pairs
    

      
    def equalPairsOpt2(self, grid: List[List[int]]) -> int:
        '''
        '''
        number_pairs = 0
        n = len(grid)
        row_dict = collections.Counter(tuple(row) for row in grid)
        for c in range(n):
            column = [grid[i][c] for i in range(n)]
            number_pairs += row_dict[tuple(column)]
        return number_pairs
        