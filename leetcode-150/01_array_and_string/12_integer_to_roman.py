"""
Start dividing the number from the highest roman number possible and store the roman number in result
if the roman number is greater than current number value, decrement the roman number
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""
        pos = 0
        while num > 0:
            while num >= values[pos]:
                no_of_division = num//values[pos]
                result += "".join([roman_symbols[pos]]*no_of_division)
                num %= values[pos]
            pos += 1

        return result

if __name__ == '__main__':
    solution = Solution()

    print(solution.intToRoman(3749))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))