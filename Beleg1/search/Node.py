class Node():
    def __init__(self):
        self.parent = None
        self.depth = 0
        self.pathcost = 0
        self.state = None
        self.action = None

    def setParent(self, node):
        self.parent = node

    def setDepth(self, depth):
        self.depth = depth

    def setPathCost(self, cost):
        self.pathcost = cost

    def setAction(self, action):
        self.action = action

    def setState(self, state):
        self.state = state

def expand(node, problem):
    successors = []
    for suc in problem.getSuccessors(node.state):
        s = Node()
        s.setParent(node)
        s.setState(suc[0])
        s.setAction(suc[1])
        s.setPathCost(node.pathcost + suc[2])
        s.setDepth(node.depth + 1)
        successors.append(s)
    return successors