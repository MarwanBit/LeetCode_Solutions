class Solution:
    #Very slow solution O(len(str1)*len(str2))
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter_str = ""
        other_str = ""
        gcd_str = ""

        #Now we check for the shortest string
        #this case work can be got rid off for cleaner code
        if len(str1) < len(str2):
            shorter_str = str1
            other_str = str2

        elif len(str2) <= len(str1):
            shorter_str = str2
            other_str = str1
        
        for index in range(len(shorter_str)):
            candidate_str = shorter_str[0:index+1]
            #Check if candidate_str is a divisor of other_str
            quotient1 = len(other_str) // len(candidate_str)
            #we must also check that candidate_str is a divisor of shorter_str
            quotient2 = len(shorter_str) // len(candidate_str)

            divides_other_str = (quotient1 == len(other_str) / len(candidate_str)) and \
            (quotient1*candidate_str == other_str)
            divides_shorter_str = (quotient2 == len(shorter_str) / len(candidate_str)) and \
            (quotient2*candidate_str == shorter_str)
                

            if (divides_other_str and divides_shorter_str):
                gcd_str = candidate_str
        
        return gcd_str
    
    def gcdOfStringsFaster(self, str1: str, str2: str) -> str:
        pass 

if __name__ == "__main__":
    solution = Solution()
    str1 = "ABAB"
    str2 = "ABDC"

    print(solution.gcdOfStrings(str1, str2))