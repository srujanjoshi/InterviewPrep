class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        inflection_point= 0 #index of min value
        if(len(nums)==1):
            pass
        elif(nums[left]<nums[right]):
            pass  
        else:
            while(left<=right):
                mid = left + (right - left)//2
                if(mid>0 and nums[mid]<nums[mid-1]):
                    inflection_point = mid
                    break
                if(mid< len(nums)-1 and nums[mid] > nums[mid+1]):
                    inflection_point = mid +1 
                    break
                if(nums[mid]> nums[right]): 
                    left= mid+1 
                else:
                    right = mid
            if(target> nums[len(nums)-1]): 
                left = 0 
                right = inflection_point -1 
            else: 
                left = inflection_point 
                right =len(nums)-1 
    
        while(left<=right): 
            mid = left+ (right -left)//2 
            if(target == nums[mid]):
                return mid
            elif(target < nums[mid]):
                right = mid-1
            else:
                left = mid +1
        
        return -1 