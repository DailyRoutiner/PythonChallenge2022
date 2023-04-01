class Solution:

    def hammingWeight(self, n: int) -> int:
        count = 0
        # bit 하나씩 읽어서 >> 쉬프트 해야한다.
        while n:
            count += n & 1
            #n = n & n - 1
            n = n >> 1
        return count


sol = Solution()
print(sol.hammingWeight("0000000000000000000001000001011"))