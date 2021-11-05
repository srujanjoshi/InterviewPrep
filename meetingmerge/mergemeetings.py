 # Input Format:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

 # Output Format: [(0, 1), (3, 8), (9, 12)]

def merge_meetings(meeting_times):

    for time_block_a in meeting_times:
        for time_block_b in [x for x in meeting_times if x!= time_block_a]:
            if(time_block_a[0] <= time_block_b[1]) and (time_block_a[1]>=time_block_b[0]):
                new_time_block= (min(time_block_a[0],time_block_b[0]),max(time_block_a[1],time_block_b[1]))
                meeting_times.remove(time_block_a)
                meeting_times.remove(time_block_b) 
                meeting_times.append(new_time_block)
    print(meeting_times)

merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])