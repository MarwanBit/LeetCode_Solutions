class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        '''
        left_ptr: int = 0
        max_vowel_count: int  = 0
        prev_vowel_count: int  = 0
        vowel_list: list[str] = ["a", "e", "i", "o", "u"]
        #first let's get the vowel count of the first sliding window
        for letter in s[left_ptr: left_ptr + k]:
            if letter.lower() in vowel_list:
                max_vowel_count += 1 
                prev_vowel_count += 1
        #interesting to look at (print(x, print(y)))
        #this establishes the vowel count, this operation is O(N) at worse
        for left_ptr in range(1, len(s) - k + 1):
            prev_char = s[left_ptr - 1]
            next_char = s[left_ptr + k - 1]
            new_count = prev_vowel_count
            if prev_char.lower() in vowel_list:
                new_count -= 1
            if next_char.lower() in vowel_list:
                new_count += 1 
            #now we update
            max_vowel_count = max(max_vowel_count, new_count)
            #now we update prev_vowel_count
            prev_vowel_count = new_count
        return max_vowel_count


if __name__ == "__main__":
    sol = Solution()
    s = "abciiidef"
    k = 3 
    #print(sol.maxVowels(s, k))
    print(sol.maxVowels("weallloveyou", 7))
