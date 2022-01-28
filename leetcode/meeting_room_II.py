import heapq
"""
meeting rooms II 
 - heaps

time: n log n
space: n

"""

# using a priority queue
'''
 1 sort by start time
 2 init a min heap, add the first meetings end time to the heap, 
 3 for every meeting rroom, check if the minimum element of the heap is free or not
 4 if the room is free then we extract the topmost element and add it back with the ending time fo the current meeting we are processing
 5 if not then we allocate a new room and addit to the heap
 6 after processing all the meetings, the size of the heap will tell us the number of rooms allocated
'''

# sort by the start time
# heapify by the end time

def minMeetingRooms(intervals):
    
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key= lambda x: x[0])

    # Add the first meeting. We have to give a new room to the first meeting. (use endtime)
    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for interval in intervals[1:]:

        # If the room due to free up the earliest is free, 
        # assign that room to this meeting.

          # minHeap         next meeting start time
          # end time
        if free_rooms[0] <= interval[0]:

            # 10 AM     vs  16 (4 PM)
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, interval[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)