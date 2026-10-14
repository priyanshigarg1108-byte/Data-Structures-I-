##LABSHEET10 
#QUES1 

# OPEN HASHING (Separate Chaining)

class OpenHashing:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]

    def display(self):
        print("\nOpen Hashing:")
        for i in range(self.size):
            print(i, ":", self.table[i])


# CLOSED HASHING (Linear Probing + Rehashing)

class ClosedHashing:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return key % self.size

    def rehash(self):
        old_table = self.table
        self.size = self.size * 2
        self.table = [None] * self.size
        self.count = 0

        for key in old_table:
            if key is not None:
                self.insert(key)

    def insert(self, key):
        # Resize when load factor reaches 0.7
        if self.count / self.size >= 0.7:
            self.rehash()

        index = self.hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key
        self.count += 1

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True

            index = (index + 1) % self.size

            if index == start:
                break

        return False

    def display(self):
        print("\nClosed Hashing:")
        for i in range(self.size):
            print(i, ":", self.table[i])


# MAIN PROGRAM

# Open Hashing
open_hash = OpenHashing()

# Closed Hashing
closed_hash = ClosedHashing()

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter element: "))
    open_hash.insert(key)
    closed_hash.insert(key)

open_hash.display()
closed_hash.display()

key = int(input("\nEnter element to search: "))

print("Open Hashing Search:", open_hash.search(key))
print("Closed Hashing Search:", closed_hash.search(key))

##QUES2


from collections import deque

# Graph Representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices

        # Adjacency Matrix
        self.matrix = [[0] * vertices for _ in range(vertices)]

        # Adjacency List
        self.adj_list = {i: [] for i in range(vertices)}

    # Add edge
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Display Adjacency Matrix
    def display_matrix(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)

    # Display Adjacency List
    def display_list(self):
        print("\nAdjacency List:")
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

    # Depth First Search (DFS)
    def DFS(self, start):
        visited = [False] * self.V
        stack = [start]
        step = 1

        print("\nDFS Traversal:")

        while stack:
            node = stack.pop()

            if not visited[node]:
                visited[node] = True
                print("Step", step, ":", node)
                step += 1

                # Reverse order to maintain natural visiting order
                for neighbor in reversed(self.adj_list[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)

    # Breadth First Search (BFS)
    def BFS(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        step = 1

        print("\nBFS Traversal:")

        while queue:
            node = queue.popleft()

            print("Step", step, ":", node)
            step += 1

            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


# Main Program
n = int(input("Enter number of vertices: "))

g = Graph(n)

e = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for i in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

g.display_matrix()
g.display_list()

start = int(input("\nEnter starting vertex: "))

g.DFS(start)
g.BFS(start)

#QUES3

# Minimum Spanning Tree using Kruskal's and Prim's Algorithms

import heapq

# ---------------- KRUSKAL'S ALGORITHM ----------------

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)

        # Avoid cycle
        if x != y:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, x, y)

        if len(mst) == vertices - 1:
            break

    if len(mst) != vertices - 1:
        print("Graph is disconnected. MST does not exist.")
        return

    print("\nKruskal's Algorithm:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Minimum Cost:", total_cost)


# ---------------- PRIM'S ALGORITHM ----------------

def prim(vertices, graph):
    visited = [False] * vertices
    min_heap = [(0, 0, -1)]

    mst = []
    total_cost = 0

    while min_heap and len(mst) < vertices - 1:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    if len(mst) != vertices - 1:
        print("\nGraph is disconnected. MST does not exist.")
        return

    print("\nPrim's Algorithm:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Minimum Cost:", total_cost)


# ---------------- MAIN PROGRAM ----------------

vertices = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
graph = {i: [] for i in range(vertices)}

print("Enter edges (u v weight):")

for i in range(e):
    u, v, w = map(int, input().split())

    edges.append((u, v, w))

    graph[u].append((v, w))
    graph[v].append((u, w))

kruskal(vertices, edges.copy())
prim(vertices, graph)

