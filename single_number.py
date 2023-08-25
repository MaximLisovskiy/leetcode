from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        try:
            new_dict = Counter(nums)
            for key, value in new_dict.items():
                if value == 1:
                    return key
        except:
            return "You need enter the list"

result = Solution()
print(result.singleNumber(1))