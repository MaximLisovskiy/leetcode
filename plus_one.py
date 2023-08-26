
class Solution(object):
    def plusOne(self, digits: list) -> list:
        number = int("".join(map(str, digits)))
        number += 1
        try:
            convert_to_string = str(number)
            list_plus_one = []
            for i in convert_to_string:
                list_plus_one.append(int(i))
            return list_plus_one
        except Exception:
            return "You need the list"

result = Solution()
print(result.plusOne([2]))

