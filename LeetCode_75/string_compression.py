class Solution:
    def compress(self, chars: list[str]) -> int:
        index = 0
        res = 0 
        while index < len(chars):
            streak = 1
            while (index + streak < len(chars)) and chars[index + streak] == chars[index]:
                streak += 1
            chars[res] = chars[index]
            res += 1
            if streak > 1:
               rep = str(streak)
               chars[res: res + len(rep)] = list(rep)
               res += len(rep)
            index += streak
        return res 