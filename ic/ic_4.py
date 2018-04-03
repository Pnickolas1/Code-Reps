

# calendar times, find a time when everyone is available

def merge_times(meetings):

    # sort meetings by start time
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current meeting overlaps with the last merged meeting, use the later of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))

        else:
            # add the current meeting since it doesnt overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    print merged_meetings



times =  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


merge_times(times)


# take aways - not able to working with greedy approach, first sort then greedy approach works
# complexity O(n lg n)