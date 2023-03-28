
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count = 0
        #
        # if low % 2 == 1:
        #     for num in range(low, high+1, 2):
        #         count = count + 1
        # else:
        #     for num in range(low+1, high+1, 2):
        #         count = count + 1
        #
        # return count
        n = (high - low) // 2
        if low % 2 == 0 and high % 2 == 0:
            return n
        return n + 1

sol = Solution()
lowNum = 798273637
highNum = 970699661
print(sol.countOdds(low=lowNum, high=highNum))