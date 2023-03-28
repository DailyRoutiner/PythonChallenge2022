class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        result = []
        sp = 1
        # 해당 원소열만 빼고 nums 다 곱하기
        for n in nums:
            result.append(sp)
            sp *= n
        post = 1
        for i, x in enumerate(reversed(nums)): # range(len(nums)-1, -1, -1)
            print(i)
            result[len(nums)-i-1] *= post
            post *= x

        return result


sol = Solution()

print(sol.productExceptSelf(nums=[1,2,3,4]))