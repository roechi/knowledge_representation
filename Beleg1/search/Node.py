class Node():
    def __init__(self):
        self.parent = None
        self.depth = 0
        self.pathcost = 0
        self.state = None
        self.action = None

def expand(node, problem):
    successors = []
    for suc in problem.getSuccessors(node.state):
        s = Node()
        s.parent = node
        s.state = suc[0]
        s.action = suc[1]
        s.pathcost = node.pathcost + suc[2]
        s.depth = node.depth + 1
        successors.append(s)
    return successors