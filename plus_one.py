
class Solution(object):
    def plusOne(self, digits: list) -> list:
        try:
            number = int("".join(map(str, digits)))
        except TypeError:
            return "You need the list"
        number += 1
        convert_to_string = str(number)
        list_plus_one = []
        for i in convert_to_string:
            list_plus_one.append(int(i))
        return list_plus_one



result = Solution()
print(result.plusOne(1))

