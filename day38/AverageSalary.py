class Solution:
    def average(self, salary: [int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)

        result = sum(salary) - max_salary - min_salary
        count = len(salary) - 2

        return result / count



sol = Solution()

print(sol.average([4000,3000,1000,2000]))