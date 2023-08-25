
class Solution(object):
    def plusOne(self, digits: list) -> list:
        number = int("".join(map(str, digits)))
        number += 1
        convert_to_string = str(number)
        list_plus_one = []
        try:
            for i in convert_to_string:
                list_plus_one.append(int(i))
            return list_plus_one
        except:
            return "You need the list"

result = Solution()
print(result.plusOne([4, 3, 2, 1]))

