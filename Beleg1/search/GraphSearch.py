import Node

def graphSearch(problem, fringe):
    solution = []
    closed = []
    root = Node.Node()
    root.setParent(None)
    root.setAction(None)
    root.setState(problem.getStartState())
    root.setPathCost(0)
    root.setDepth(0)

    fringe.push(root)
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.state):
            current = node
            solution = []
            while (not(current.parent is None)):
                solution.append(current.action)
                current = current.parent
            solution.reverse()
            return solution
        else:
            if (not closed.__contains__(node.state)):
                closed.append(node.state)
                for n in Node.expand(node, problem):
                    fringe.push(n)
    return []
