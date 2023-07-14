class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth = 0 
        stack = []
        for char in s:
            print("stack", stack)
            print("char", char)
            if char == "(":
                stack.append(char)
                print("appending (")
                print(s)
            elif stack and char == ")" and stack[-1] == "(":
                stack.pop()
                nesting_depth += 1
                print("Popping!!!")
                print(stack)
        return nesting_depth
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))