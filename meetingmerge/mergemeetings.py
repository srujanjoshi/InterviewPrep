 # Input Format:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

 # Output Format: [(0, 1), (3, 8), (9, 12)]



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

