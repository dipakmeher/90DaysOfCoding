#DFS Implementation
from collections import defaultdict

class Graph:
    #Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self,v):
        queue = list()
        visited = set()
        BFSSequence = list()
        
        queue.append(v)
        print("Sizeof: ", queue.__sizeof__)
        while(len(queue)!= 0):
            currentNode = queue.pop(0)
            BFSSequence.append(currentNode)
            if(currentNode not in visited):
                visited.add(currentNode)
                print("visited: ", visited)
            
            for neighbour in self.graph[currentNode]: # g.graph stores the adjacency list for each node
                if neighbour not in visited:
                    queue.append(neighbour)
        print(BFSSequence)


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




