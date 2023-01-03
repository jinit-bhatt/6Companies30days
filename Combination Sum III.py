class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result =[]
        self.adding([],1,k,n)
        return self.result
    
    def adding(self,path,start,k,n):
        
        if k ==0 and n==0:
            self.result.append(path)
            return 
        
        if k == 0 or n <= 0:
            return
        
        for i in range(start,10):
            self.adding(path+[i],i+1,k-1,n-i)
