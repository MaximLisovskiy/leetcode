
class Solution(object):
    def plusOne(self, digits):
        number = int("".join(map(str, digits)))
        number += 1
        new_list = str(number)
        new_list_1 = []
        for i in new_list:
            new_list_1.append(int(i))
        return new_list_1

result = Solution()
print(result.plusOne([4, 3, 2, 1]))