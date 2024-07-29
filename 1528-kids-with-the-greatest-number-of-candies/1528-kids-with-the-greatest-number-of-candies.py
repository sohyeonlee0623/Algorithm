class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result

# Example usage:
solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [true,true,true,false,true]
print(solution.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [true,false,false,false,false]
print(solution.kidsWithCandies([12, 1, 12], 10))     # Output: [true,false,true]