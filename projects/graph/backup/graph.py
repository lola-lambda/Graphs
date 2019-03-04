"""
Simple graph implementation compatible with BokehGraph class.
"""
class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop()
    else:
      return None

class Stack:
  def __init__(self):
    self.storage = []
  
  def push(self, item):
    self.storage.append(item)

  def pop(self):
    return self.storage.pop()

class Graph:
    """The graph itself is simply a set of vertices."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex DNE")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex DNE")

    def bft(self, starting):
        q = Queue()
        visited = set()
        q.enqueue(starting)
        while q.size > 0:
            next = q.dequeue()
            if next not in visited:
                visited.add(next)
                print(next)
                for child in self.vertices[next]:
                    q.enqueue(child)
        # create an empty queue
        # create an empty set of visited vertices
        # enqueue the starting index
        # while queue is not empty
            # dequeue
            # if it has not been visited
                # add it to visited vertex set
                # enqueue the children
    
    def dft(self, starting):
        s = Stack()
        visited = set()
        s.push(starting)
        while len(s.storage) > 0:
            next = s.pop()
            if next not in visited:
                visited.add(next)
                print(next)
                for child in self.vertices[next]:
                    s.push(child)
        # create an empty stack
        # create an empty set of visited vertices
        # add the starting index to the stack
        # while stack is not empty
            # remove from stack
            # if it has not been visited
                # add it to visited vertex set
                # add the children to the stack

    def dft_recursive(self, current, visited=set()):
        visited.add(current)
        print(current)
        for child in self.vertices[current]:
            if child not in visited:
                self.dft_recursive(child, visited)
        
    def bfs(self, starting, destination):
        q = Queue()
        visited = set()
        q.enqueue(starting)
        while q.size > 0:
            next = q.dequeue()
            if next is destination:
                visited.add(next)
                print(visited)
                return
            elif next not in visited:
                visited.add(next)
                for child in self.vertices[next]:
                    q.enqueue(child)

    def dfs(self, current, destination, visited=set()):
        visited.add(current)
        for child in self.vertices[current]:
            if child is destination:
                visited.add(child)
                print(visited)
            elif child not in visited:
                self.dfs(child, destination, visited)
           
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

print('bft', graph.bft('0'))
print('iterative dft', graph.dft('0'))
print('recursive dft', graph.dft_recursive('0'))
print('bfs', graph.bfs('3', '1'))
print('dfs', graph.dfs('3', '1'))