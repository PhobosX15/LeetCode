class Solution:
    def WiggleSort(self,num):
        #convert num to a set
        num_copy= sorted(num)
        #split the list into two halves rounding up



        low= num_copy[:round(len(num_copy)/2)]
        high= num_copy[round(len(num_copy)/2):]
        for i in range(len(low)):
            num[2*i]= low[i]
            if 2*i+1<len(num):
                num[2*i+1]= high[i]
        
        return num
    
if __name__ == "__main__":
    num=[1,2,1,2,1,3,4]
    result= Solution().WiggleSort(num)
    print(result)
        