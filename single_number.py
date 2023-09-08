from collections import Counter

class Solution(object):
    def singleNumber(self, nums: list) -> int:
        try:
            new_dict = Counter(nums)
        except:
            return "You need enter the list"
        for key, value in new_dict.items():
            if value == 1:
                return key

result = Solution()
print(result.singleNumber([1, 2, 1, 2, 4]))
