 # Input Format:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

 # Output Format: [(0, 1), (3, 8), (9, 12)]

def merge_meetings_on2(meeting_times):

    for time_block_a in meeting_times:
        for time_block_b in [x for x in meeting_times if x!= time_block_a]:
            if(time_block_a[0] <= time_block_b[1]) and (time_block_a[1]>=time_block_b[0]):
                new_time_block= (min(time_block_a[0],time_block_b[0]),max(time_block_a[1],time_block_b[1]))
                meeting_times.remove(time_block_a)
                meeting_times.remove(time_block_b) 
                meeting_times.append(new_time_block)
    print(meeting_times)


def merge_meetings(meeting_times):
    meeting_times.sort(key= lambda a: a[0])
    i=0
    while (i<len(meeting_times)-1):
        if(meeting_times[i][1]>= meeting_times[i+1][0]):
            new_time_block= (meeting_times[i][0],max(meeting_times[i][1],meeting_times[i+1][1]))
            meeting_times[i]=new_time_block
            meeting_times.remove(meeting_times[i+1])
        else:
            i+=1
    return(meeting_times)

merge_meetings([(1, 4), (2, 5), (5, 8)])

