from collections import deque
from time import sleep

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        '''
        senate_length = 0
        senate_que = deque()
        #fill our que
        for char in senate:
            senate_length += 1
            senate_que.append(char)
        while True:
            senator = senate_que[0]
            #Check if we've eliminated all the other senators
            if senator == "R" and "D" not in senate_que: return "Radiant"
            if senator == "D" and "R" not in senate_que: return "Dire"
            # if not we look for the next senator of the opposite party
            i = 0
            foundMatch = False 
            #first we pop our current senator to simulate them finishing the vote
            senate_que.popleft()
            senate_que.append(senator)
            length = len(senate_que)
            while not foundMatch and i < length - 2:
                if senator == "R" and senate_que[i] == "C":
                    senate_que.popleft()
                    foundMatch = True 
                elif senator == "C" and senate_que[i] == "R":
                    senate_que.popleft()
                    foundMatch = True
                #Other wise we need to keep looking
                else:
                    i += 1 

