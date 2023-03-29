ROMAN = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        replace_num = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            replace_num += ROMAN[char]
            print(replace_num)
        #print(replace_num)

sol = Solution()

sol.romanToInt("MCMXCIV")