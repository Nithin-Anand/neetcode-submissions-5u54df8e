class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid_spaces = 0
        empty_sequence = 0

        if flowerbed[0] == 0:
            empty_sequence = 1

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                empty_sequence += 1
            else:
                if empty_sequence >= 3:
                    valid_spaces += ((empty_sequence - 1) // 2)
                empty_sequence = 0

            # if empty_sequence == 3:
            #     valid_spaces += 1
            #     empty_sequence = 0
            


        if empty_sequence == 2:
            valid_spaces += 1
        
        if n <= valid_spaces:
            return True
        
        return False