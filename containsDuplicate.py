class Solution(object):
    def containsDuplicate(self, nums):
        return True if len(set(nums)) < len(nums) else False

result = Solution()
print(result.containsDuplicate([2, 3, 4, 5, 6]))