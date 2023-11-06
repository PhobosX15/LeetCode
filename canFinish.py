from collections import defaultdict


class Solution:
    def canFinish(self,numCourses, prerequisites):
        #create a dictionary of courses and their prerequisites
        course_dict={}
        

        if len(prerequisites)==0:
            return True
        for i in range(len(prerequisites)):
            if prerequisites[i][0]==prerequisites[i][1]:
                    return False
            if prerequisites[i][0] not in course_dict:
                course_dict[prerequisites[i][0]]=[prerequisites[i][1]]
            else:
                course_dict[prerequisites[i][0]].append(prerequisites[i][1])

        #create a set from list prerequisites
        prerequisites_list=[item for sublist in prerequisites for item in sublist]
        prerequisites_set=set(prerequisites_list)
        #iterate through the set and check if the course has any prerequisites
        count=0
        accept=False
        flag, completed_courses, checked_courses= False, {}, {}
        for item in prerequisites_set:
            flag,completed_courses,checked_courses= self.check_precourse(course_dict, completed_courses,item,checked_courses,item)
            if flag:
                accept=True
                completed_courses[item]=1
                count=count+1    

        if count==len(prerequisites_set) and count<=numCourses and accept:
            return True
        else:  
            return False
        
     #function to check if the pre-requisite course is completed through recursion   
    def check_precourse(self, course_dict, completed_courses,course,checked_courses,item,dummy=-1):
       
        if course not in course_dict:
            dummy=1
            completed_courses[course]=1

            return True, completed_courses, checked_courses

        else:
            for pre_course in course_dict[course]:
                if pre_course not in checked_courses and pre_course not in completed_courses:
                        checked_courses[pre_course]=1
                        dummy=1
                        flag, completed_courses, checked_courses= self.check_precourse(course_dict, completed_courses,pre_course,checked_courses,item)

                        if (not flag):
                            return False, completed_courses, checked_courses
                        
                if all(course in list(completed_courses.keys()) for course in course_dict[course]):
                        completed_courses[course]=1
                        return True, completed_courses, checked_courses
                            
                """ elif pre_course in completed_courses and pre_course not in checked_courses:
                    continue
                else:
                    if pre_course in checked_courses:
                        dummy=1
                        return False, completed_courses, checked_courses """
                        
                    
                            
            if dummy==-1:
                return False, completed_courses, checked_courses
                    
            check_list=course_dict[item]
            #bcheck_list.append(item)     
            print(check_list)
          
            if check_list==None or all(i in list(completed_courses.keys()) for i in check_list):
                
                return True, completed_courses, checked_courses
            else:
                return False, completed_courses, checked_courses
        

if __name__ == "__main__":
    numCourses=2

    prerequisites=[[0,1],[1,0]]
    result= Solution().canFinish(numCourses, prerequisites)
    print(result)
                    