class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak=arr[0]
        for i in range (1,len(arr)-1):
            if(arr[i]>arr[i+1] and arr[i]>arr[i-1]):
                temp=i
                if(arr[temp]>peak):
                    peak=temp
        if(arr[len(arr)-1]>arr[peak]):
            peak=len(arr)-1
        return peak
            
