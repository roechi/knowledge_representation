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

