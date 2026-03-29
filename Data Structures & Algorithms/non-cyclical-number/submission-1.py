class Solution:
    def isHappy(self, n: int) -> bool:
        seen_elements = {}

        cycle = False
        val = n
        while not cycle:
            sum_of_digit_squares = 0
            string_val = str(val)
            for i in string_val:
                sum_of_digit_squares += int(i) ** 2
            
            if sum_of_digit_squares == 1:
                return True
            else:
                if seen_elements.get(sum_of_digit_squares, 0) == 1:
                    return False
                else:
                    seen_elements[sum_of_digit_squares] = 1
            val = sum_of_digit_squares
            
