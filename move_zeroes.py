class Solution:
    def moveZeroes(self, nums: list) -> list:
        try:
            zero_list = [i for i in nums if i == 0]
        except Exception:
            return "Enter the list"
        for i in zero_list:
            nums.remove(i)
            nums.append(0)
        return nums

result = Solution()
print(result.moveZeroes([0, 1, 3, 0, 12]))