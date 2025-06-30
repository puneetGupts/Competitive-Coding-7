from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #sort based on start and end and prepare two list
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        n = len(start)
        res = 0
        endi = 0
        starti =0
        while starti< n:
            # do we need a room compare start[i] with end[i] and move start alwasy but move end onl when start[i] > end 
            if start[starti] < end[endi]:
                res+=1
                starti+=1
            else:
                starti+=1
                endi+=1
        return res

import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Min-heap to track end times
    heap = []  # stores end times

    for interval in intervals:
        start, end = interval

        # If the room is free (earliest end time ≤ current start), reuse it
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        # Allocate a new room (or re-use popped one)
        heapq.heappush(heap, end)

    # Step 3: The size of the heap tells us the number of rooms needed
    return len(heap)
