from collections import defaultdict
import numpy as np
import random
import math


 

class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
 
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
 
    def printGraph(self):
        for i in range(self.v):
            print("src=",i)
            for j in self.graph[i]:
                print(j)

    def isReachable(self,src,dest):
        visited =[False]*(self.v+1)

        queue=[]                       
        queue.append(src)              

        visited[src] = True
        while queue:
            n = queue.pop(0)            
            if n == dest:
                   return True
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
 
        for j in self.graph[v]:
            if j not in visited:
                self.DFSUtil(j, visited)
 
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)



# GET INPUT FUNCTION and COVERT TO GRAPH
file_address = "C:/Users/Ashkan/Desktop/Term 8/هوش/تمرین ها/تمرین 2 - بخش اول/SA/input.txt"

lines = []
with open(file_address) as f:
    lines = f.readlines() 

V = int(lines[0])
graph = Graph(V+1)
count = 0
for line in lines:
    if(count!=0):
        edge = line.split(' ')
        graph.addEdge(int(edge[0]),int(edge[1]))
    count += 1
  


# OBJECTIVE FUNCTION
def objective(sol):
    q = 0
    for i in range(n): # 3 4 12 5
        for j in range(i,n):
            if(graph.isReachable(sol[j],sol[i]) and i!=j):
                q = q + 1
    return q


# INITIAL DATA & PARAMETERS
n = V
T = 100000
t_change = 0.99

# INITIAL SOLUTION
sequence = [i+1 for i in range(n)]
solution = random.sample(sequence, n)
print(solution)
fitness = objective(solution)
print(fitness)

# MAIN LOOP OF SA ALGORITHM
while T > 0:
    neighbour = solution.copy()
    temp = np.random.randint(n)
    temp2 = np.random.randint(n)
    if((graph.isReachable(neighbour[temp],neighbour[temp2]) and temp<temp2)):
        continue
    

    neighbour[temp] , neighbour[temp2] = neighbour[temp2] , neighbour[temp]

    fit = objective(neighbour)

    delta = fitness - fit
    if delta >= 0:
        solution = neighbour
        fitness = fit
    else:
        pr = math.exp(delta / T)
        if pr >= .999:
            solution = neighbour
            fitness = fit

    #print(fitness)
    T = int(T * t_change)


print(solution)
print(fitness)
