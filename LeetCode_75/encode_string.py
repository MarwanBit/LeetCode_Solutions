class Solution:
    def decodeString(self, s: str) -> str:
        '''
        '''
        stack = []
        for char in s:
            print("Beginning of the loop")
            print(stack)
            print("this is the current char: ", char)
            s = ""
            num_str = ""
            if char != "]":
                stack.append(char) 
                print("appended char with no issues")
                print(stack)
            elif char == "]":
                print("hit ], going to go back on the stack now")
                while stack and stack[-1] != "[":
                    print("current s being built")
                    s = stack.pop() + s
                    print(s)
                print("pop the []")
                stack.pop()
                print("This is the string we built")
                print(s)
                print("stack after looping back")
                print(stack)
                print("now we are getting the number in front")
                while stack and stack[-1].isdigit():
                    print("updating num")
                    num_str = stack.pop() + num_str
                    print("num_str: ", num_str)
                print("current_num_str and stack: ", num_str)
                print("stack: ", stack)
                stack.append(int(num_str)*s)
        return "".join(stack)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))