class Solution(object):
    def containsDuplicate(self, nums: list) -> bool:
        try:
            return True if len(set(nums)) < len(nums) else False
        except:
            return "Enter the list"


result = Solution()
print(result.containsDuplicate([1, 2, 3, 4]))