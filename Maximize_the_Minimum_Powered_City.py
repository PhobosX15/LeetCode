#pip install pulp
from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, lpSum

class min_power:

    def __init__(self,stations, r,k):
        self.stations = stations
        self.r = r
        self.k = k

    def find_power(self,stations,r):
        power=[]
        for index,station in enumerate(stations):
            temp=[stations[index+i] for i in range(-r,r+1) if index+i<len(stations) and index+i>=0]
            power.append(sum(temp))
            
        return power
    
    def optimize(self,stations,r,k):
        model= LpProblem(name="min_power", sense=LpMaximize)
        problem_list=[]
        for i in range(len(stations)):
            x=LpVariable(name=f"problem_{i}", lowBound=0, upBound=1, cat="Integer")
            x.setInitialValue(0)
            problem_list.append(x)
        
        #define objective function as the minimum value in power list
        stations=[stations[i]+problem_list[i].varValue for i in range(len(stations))]
        power=self.find_power(stations,r)
        model += lpSum(min(power))

        #define constraints
        model+=lpSum(problem_list)==k
        #non negative constraint
        for i in range(len(stations)):
            model+=problem_list[i]>=0
        #solve
        status = model.solve()
        print(LpStatus[status])


if __name__ == "__main__":
    stations=[1,2,3,4,5,6,7,8,9,10]
    r=2
    k=3
    min_power= min_power(stations,r,k)
    min_power.optimize(stations,r,k)
