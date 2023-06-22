import time

class Solution:
    def getWordList(self, s: str) -> str:
        #first let's preprocess the string
        s = s.strip()
        word_list = [] 
        start = 0
        end = 0 

        #Edge case where the string is one letter
        if len(s) == 1:
            return [s]

        while (start != len(s) - 1) and (end != len(s) - 1):
            while s[start] == " ":
                start += 1
                end += 1
            while ((s[end] != " ") or (end == start)) and (end != len(s) - 1):
                end += 1
            word = s[start : end]
            if end == len(s) - 1:
                word = s[start: end + 1]
            word_list.append(word)

            #now we move on to the next word if we can
            start = end

        return word_list


    def reverseWords(self, s: str) -> str:
        word_list = self.getWordList(s)
        output_str = ""
        #iterate through out word_list!
        for index in range(len(word_list) - 1, -1, -1):
            output_str += (word_list[index] + " ")
        return output_str[0: len(output_str) - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.getWordList(" Hello World!"))
    print(sol.reverseWords("Hello World!"))