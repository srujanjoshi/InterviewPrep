class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        new_interval= newInterval
        for i,interval in enumerate(intervals):
            if not new_interval:
                ret.append(interval)
                continue
            #If new interval ends before the current interval starts, add the new
            #interval, the current interval and the remaining intervals to the return list
            if(new_interval[1]<interval[0]):
                ret.append(new_interval)
                ret.append(interval)
                new_interval = []
                continue
            #If the new interval starts after the current interval ends, add the current interval to
            #the return list and continue
            if(new_interval[0] > interval[1]):
                ret.append(interval)
                continue
            
            #If both of the above cases are false, then the new interval overlaps with the current
            #interval. In that case, merge the two intervals and continue
            new_interval = [min(new_interval[0],interval[0]),max(new_interval[1],interval[1])]
            
            
            
        if new_interval:
            ret.append(new_interval)
            
        return ret