class Solution:
    def isValid(self, s: str) -> bool:
        '''
        O(n) time, O(n) space
        '''
        stack = []
        parenthesis_dict = {"(" : ")",
                            "[" : "]", 
                            "{" : "}"}
        for index, char in enumerate(s):
            #Add open parenthesis
            if char in parenthesis_dict:
                stack.append(char)
            else:
                #if the stack is empty and we add a }, ), ]
                # it is invalid
                if not stack:
                    return False
                elif parenthesis_dict[stack[-1]] == char:
                    stack.pop()
                #there is no matching parenthesis :(
                else:
                    return False
        return not stack
            