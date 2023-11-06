from math import *
from typing import List


def find_spots(x:int,y:int,k:int, diner:List[int]) -> List[int]:

    if (x==-1 or y==len(diner)) and (y+1)-(x+1)-1<k+1:
        return diner
    
    
    elif x==-1:
        if (y+1)-(x+1)-1>=k+1:
            diner[0]=1
            find_spots(x+1,y,k,diner)
            return diner


    elif y==len(diner):
        if y-x-1>=k+1:
            diner[len(diner)-1]=1
            find_spots(x,y-1,k,diner)
            return diner

    elif y-x-1>=(2*k)+1:
        mid = floor((x+y)/2)
        diner[mid]=1
        find_spots(x,mid,k,diner)
        find_spots(mid,y,k,diner)
        return diner

    elif y-x-1<2*k+1:
        return diner
    
    
    


# N is number of spots
# M is number of diners sitting
# K is number of social distancing spots
# S is list containing the spots of the diners sitting
def getMaxAdditionalDiners(N :int, K:int, M:int,S:List[int]) -> int:
    S.extend([0,N+1])
    S.sort()

    #build the array
    diner=[0 if i not in S else 1 for i in range(1,N+1)]
   
        

    for i in range(0,len(S)-1):
        y= S[i+1]
        x= S[i]
        diner=find_spots(x-1,y-1,K, diner)
    return sum(diner)-M

print(getMaxAdditionalDiners(15, 1, 3, [11, 12, 14]))


       
