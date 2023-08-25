from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        new_dict = Counter(nums)
        for key, value in new_dict.items():
            if value == 1:
                return key

result = Solution()
print(result.singleNumber([4, 1, 2, 1, 2]))