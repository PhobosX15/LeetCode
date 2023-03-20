#pip install pulp
from collections import defaultdict


class minimize():
    def __init__ (self, stations, r, k) -> None:
        self.stations = stations
        self.r = r
        self.k = k
    
    def check(self,stations,r,k,mid)-> bool:
        sliding_window= sum(stations[:2*r]) 
        hashmap= defaultdict(int)
        index=r
        while index< len(stations)-r:
            sliding_window+= stations[index+r]
            if sliding_window<mid:
                diff= abs(sliding_window-mid)
                if diff>k:
                    return False
                else:
                    sliding_window+=diff
                    hashmap[index+r]=diff
                    k-=diff
            sliding_window-= (stations[index-r]+hashmap[index-r])
            index+=1
        return True

    def solve(self, stations, r,k) -> int:
        min_sol= min(stations)
        max_sol= sum(stations)+k
        #add 0's to the beginning and end of the list
        stations=[0]*r+stations+[0]*r
        result=min_sol
        while min_sol<=max_sol:
            mid=(min_sol+max_sol)//2
            if self.check(stations,r,k,mid):
                result= mid
                min_sol=mid+1
            else:
                max_sol=mid-1
        return result
    
if __name__ == "__main__":
    stations=[4,2]
    r=1
    k=1
    min_power= minimize(stations,r,k)
    result= min_power.solve(stations,r,k)
    print(result)
