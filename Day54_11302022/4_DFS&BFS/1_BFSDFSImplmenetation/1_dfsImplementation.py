#DFS Implementation
from collections import defaultdict

class Graph:
    #Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self,v):
        stack = list()
        visited = set()
        DFSSequence = list()
        
        stack.append(v)

        while(len(stack) != 0):
            currentNode = stack.pop()
            DFSSequence.append(currentNode)
            if(currentNode not in visited):
                visited.add(currentNode)
                print("visited: ", visited)
            
            for neighbour in self.graph[currentNode]: # g.graph stores the adjacency list for each node
                if neighbour not in visited:
                    stack.append(neighbour)
        print(DFSSequence)


if __name__=="__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)

    print(g.graph)

    g.DFS(2)




