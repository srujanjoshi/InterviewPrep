class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort the list of intervals based on the first element in the interval.
        intervals.sort(key = lambda x: x[0])
        ret = []
        i = 0
        new_interval = []
        while(i<len(intervals)):
            if not new_interval:
                new_interval= intervals[i]
                continue
            #if new interval ends before the current interval, add the new interval to 
            #the return list
            if(new_interval[1]<intervals[i][0]):
                ret.append(new_interval)
                new_interval= []
                continue
            new_interval = [min(new_interval[0],intervals[i][0]), max(new_interval[1],intervals[i][1])]
            i+=1
            
        #At the end, we either end up with a new_interval ta
        if new_interval: 
            ret.append(new_interval)
        else:
            ret.append(intervals[-1])
        
        return ret