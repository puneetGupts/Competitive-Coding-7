from typing import List
import heapq
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         max_heap = []

#         for row in matrix:
#             for num in row:
#                 heapq.heappush(max_heap, -num)  # insert negative to simulate max heap
#                 if len(max_heap) > k:
#                     heapq.heappop(max_heap)  # pop the largest among the smallest k seen so far

#         return -max_heap[0]  # return the kth smallest (negated back)

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
        
#         def count_less_equal(mid):
#             count = 0
#             row = n - 1
#             col = 0
            
#             while row >= 0 and col < n:
#                 if matrix[row][col] <= mid:
#                     count += row + 1  # All elements in this row up to 'row' are ≤ mid
#                     col += 1
#                 else:
#                     row -= 1
#             return count

#         low = matrix[0][0]
#         high = matrix[n - 1][n - 1]

#         while low < high:
#             mid = (low + high) // 2
#             if count_less_equal(mid) < k:
#                 low = mid + 1
#             else:
#                 high = mid

#         return low

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
    
        def count_less_equal(mid):
            count = 0
            col = n - 1
            row = 0
            
            while col >= 0 and row < n:
                if matrix[row][col] <= mid:
                    count += col + 1  # All elements in this col up to 'col' are ≤ mid
                    row += 1
                else:
                    col -= 1
            return count

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
