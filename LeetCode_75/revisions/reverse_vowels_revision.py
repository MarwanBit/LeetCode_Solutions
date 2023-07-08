import time

class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        The way that we can solve this problem is through a 2 pointer approach,
        where we point one pointer at the first value and then continue to iterate 
        the next pointer until we reach a vowel, we then switch the pointers and then 
        continue to iterate through the string

        This approach should be O(N) time complexity since we iterate through the 
        string once, and O(1) storage complexity since we just need to store the 
        left_ptr, right_ptr, and vowel_list, which take constant storage complexity.
        '''
        s = list(s)
        left_ptr = 0 
        right_ptr = 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        while (left_ptr < len(s) - 1):
            #Iterate till we find a vowel
            print(left_ptr, right_ptr)
            time.sleep(1)
            while(s[left_ptr].lower() not in vowel_list) and (left_ptr < len(s) - 1):
                left_ptr += 1 
                right_ptr += 1 
                print("Iterating left_ptr")
                print(left_ptr, right_ptr)
                time.sleep(1)
            while (right_ptr == left_ptr and right_ptr < len(s) - 1) or (right_ptr < len(s) - 1 and s[right_ptr].lower() not in vowel_list):
                right_ptr += 1 
                print("Iterating Right Ptr")
                print(left_ptr, right_ptr)
                time.sleep(1)
            #now if we find a valid pair we perform the swapping
            if (left_ptr != right_ptr) and (s[left_ptr].lower() in vowel_list) and (s[right_ptr].lower() in vowel_list):
                s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
                #afterwards we swap the indices of the ptrs and set them equal
                left_ptr, right_ptr = right_ptr, left_ptr
                right_ptr = left_ptr
                print("Found Valid Pair")
                print(left_ptr, right_ptr)
                time.sleep(1)
            #otherwise if we don't find a pair we set left_ptr = len(s) - 1
            else:
                left_ptr, right_ptr = right_ptr, left_ptr
                right_ptr = left_ptr

        return "".join(s)
    

    def reverseVowelsOpt(self, s: str) -> str:
        '''
        The way that we can solve this problem is through a 2 pointer approach,
        where we point one pointer at the first value and then continue to iterate 
        the next pointer until we reach a vowel, we then switch the pointers and then 
        continue to iterate through the string

        This approach should be O(N) time complexity since we iterate through the 
        string once, and O(1) storage complexity since we just need to store the 
        left_ptr, right_ptr, and vowel_list, which take constant storage complexity.
        '''
        s = list(s)
        left_ptr : int = 0 
        right_ptr: int = len(s) - 1
        vowel_list: list[str] = ['a', 'e', 'i', 'o', 'u']
        while left_ptr < right_ptr:
            print("Set Up!")
            print(left_ptr, right_ptr)
            left_char, right_char = s[left_ptr].lower(), s[right_ptr].lower()
            print(left_char, right_char)
            if left_char in vowel_list and right_char in vowel_list:
                print("Successful Pair, performing the swap")
                #perform the swap
                s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
                print(s)
                left_ptr += 1 
                right_ptr -= 1
                print(left_ptr, right_ptr)
            if left_char not in vowel_list:
                print("left_char not vowel, iterating")
                left_ptr += 1 
                print(left_ptr, right_ptr)
            if right_char not in vowel_list:
                print("right_char not vowel, iterating")
                right_ptr -= 1 
                print(left_ptr, right_ptr)
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    s = "hello"
    print(sol.reverseVowelsOpt(s))

