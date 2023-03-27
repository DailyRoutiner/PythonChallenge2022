
# valueMap[v] = valueMap.get(v, key)
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        valueMap = {}

        for key, v in enumerate(nums):
            # value값을 합해서 target 값 으로 어떻게 확인하지..? 아래처럼 차이나는 값을 찾는다.
            diff = target - v
            if diff in valueMap: #어떻게 if문 안에 딕셔너리 키값을 조회하는 건가
                return [valueMap[diff], key]
            valueMap[v] = key

sol = Solution()

print(sol.twoSum(nums=[2, 7, 11, 15], target=9))