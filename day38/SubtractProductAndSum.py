class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strNum = str(n)
        multiply = 1
        add_num = 0
        for num in strNum:
            multiply *= int(num)
            add_num += int(num)

        return multiply - add_num



sol = Solution()
print(sol.subtractProductAndSum(4421))