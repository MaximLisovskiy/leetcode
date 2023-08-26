from collections import Counter

class Solution(object):
    def singleNumber(self, nums: list) -> int:
        new_dict = Counter(nums)
        try:
            for key, value in new_dict.items():
                if value == 1:
                    return key
        except Exception:
            return "You need enter the list"

result = Solution()
print(result.singleNumber([1, 2, 2, 1, 4]))
