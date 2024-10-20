# add edges and vertix in the graph
# display grpah


class Graph:
    def __init__(self):
        self.graph ={}
    
    def add_edge(self,vertex,edge,bidirection=False):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        if edge not in self.graph:
            self.graph[edge]=[]
        self.graph[vertex].append(edge)
        if bidirection:
            self.graph[edge].append(vertex)
            
    def display(self):
        result = ""
        for key in self.graph:
            result +=  f"{key} --> {self.graph[key]}\n"
        print(result)
            
  
g = Graph()
g.add_edge(3,5,True)
g.add_edge(5,6,True)
g.add_edge(6,7,False)
g.display()
