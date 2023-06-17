import re

STR = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formal_letter = ""
        rear_letter = ""
        # 공백, 숫자, 문자 제거
        new_str = re.sub(r"[^a-zA-Z0-9\\s+]","", s).lower()

        # 처음과 끝에 번갈아가며 포인터를...
        for i in range(len(new_str)):
            formal_letter = new_str[i]
            rear_letter = new_str[-i-1]
            print(f"compare {formal_letter} ? {rear_letter}")
            if formal_letter != rear_letter:
                return False

        return True






sol = Solution()
print(sol.isPalindrome(STR))