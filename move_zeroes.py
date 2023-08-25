class Solution:
    def moveZeroes(self, nums):
        zero_list = [i for i in nums if i == 0]
        for i in zero_list:
            nums.remove(i)
            nums.append(0)
        return nums

result = Solution()
print(result.moveZeroes([0, 1, 0, 3, 12]))