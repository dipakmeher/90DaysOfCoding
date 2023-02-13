# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have 
# finished course 0. So the correct course order is [0,1].

# So if we connect the prereq with the courses then it will form a graph.
# So, basically we have to traverse a graph to find the possible order to take the courses
# we can do that using DFS

#Functions
# def courseSchedule(numCourses, prerequisites):
#     a = prerequisites[0][1]
#     stack = []
#     # stack.append("")
#     # while(len(stack) != 0):
#     for order in prerequisites:
#         if(order[1] not in stack):
#             stack.append(order[1])
#             if(order[0] not in stack):
#                 stack.append(order[0])
#     print(stack)

def courseSchedule(numCourses,prerequisites):
    #Since its a graph problem, its better to make an adjacency list
    prereq = {i:[] for i in range(numCourses)}
    for course,pre in prerequisites:
        prereq[course].append(pre)
    print(prereq)

    #Now, strategy:
    # if 0->1 and 1->0 then we can't decide which course to take. We will return false
    # This represents a cycle. We don't want cycle in a graph. 

    visited, cycle = set(), set()
    output = []
    def dfsNeighbor(course):
        if course in cycle:
            return False
        if course in visited:
            return True

        cycle.add(course)
        for pre in prereq[course]: # This step is to check the cycle basically
            if dfsNeighbor(pre) == False:
                return
        cycle.remove(course)
        visited.add(course)
        output.append(course)
        return True

    for c in range(numCourses):
        if dfsNeighbor(c) ==  False:
            return []
    
    return output
            
#Driver code
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
res = []

print(courseSchedule(numCourses,prerequisites))