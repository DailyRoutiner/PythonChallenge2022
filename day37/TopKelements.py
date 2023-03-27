class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        # Count frequent value
        count = {}
        for value in nums:
            count[value] = 1 + count.get(value, 0)

        # 어떻게 많은 값 순으로 정렬할까?
        sorted_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(sorted_list)
        return list(count.keys())[:k]

sol = Solution()

print(sol.topKFrequent(nums=[1,1,2,2,2,3], k=2))