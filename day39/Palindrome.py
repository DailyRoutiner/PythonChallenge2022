
STR = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formal_letter = ""
        rear_letter = ""
        # 공백, 숫자, 문자 제거
        #s.replace()...

        # 처음과 끝에 번갈아가며 포인터를...
        for i in range(len(s)):
            formal_letter = s[i]
            rear_letter = s[-i-1]
            print("formal " + formal_letter)
            print("rear " + rear_letter)
            if formal_letter != rear_letter:
                return False

        return True






sol = Solution()
print(sol.isPalindrome(STR))