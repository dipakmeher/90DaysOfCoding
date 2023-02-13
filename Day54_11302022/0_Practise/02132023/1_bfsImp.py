from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):
        queue = []
        visited = []
        BFSSequence = []

        queue.append(v)
        while(queue):
            curr = queue.pop(0) # Pop the first element
            BFSSequence.append(curr)
            if curr not in visited:
                visited.append(curr)
                print("Visited: ",visited)
            
            for neighbour in self.graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
        print(BFSSequence)


#Driver Code
if __name__ == "__main__":
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

    g.BFS(2)


