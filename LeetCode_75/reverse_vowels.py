class Solution:
    #times out for some weird reason
    def reverseVowels(self, s: str) -> str:
        vowels_list = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        i = 0
        j = 0
        while (i != len(s) - 1):
            i_char = s[i].lower()
            #if i_char is a vowel we fix a pointer there and start moving the j pointer
            if i_char in vowels_list:
                j = i + 1
                j_char = s[j].lower()
                if j_char in vowels_list:
                    s[i] = j_char
                    s[j] = i_char
                    #swap the values of i and j
                    i, j = j, i
                    j = i
                else:
                    while (j_char not in vowels_list) and (j != len(s) - 1):
                        j += 1
                        J_char = s[j].lower()
                        if j_char in vowels_list:
                            s[i] = j_char
                            s[j] = i_char
                            #swap the values of i and j
                            i, j = j, i
                            j = i
        return "".join(s)

    def reverseVowelsCorrect(self, s: str) -> str:
        VOWELS: set = {'a', 'e', 'i', 'o', 'u'}
        s: list[str] = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            start_val, end_val = s[start].lower(), s[end].lower()
            if start_val in VOWELS and end_val in VOWELS:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif start_val in VOWELS and end_val not in VOWELS:
                end -= 1
            elif start_val not in VOWELS and end_val in VOWELS:
                start += 1
            else:
                start += 1
                end -= 1

        return "".join(s)

    
    

if __name__ == "__main__":
    sol = Solution()
    s = "aeiou"
    print(sol.reverseVowelsCorrect(s))
    s = "hello"
    print(sol.reverseVowelsCorrect(s))