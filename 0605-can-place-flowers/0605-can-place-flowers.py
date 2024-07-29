class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n