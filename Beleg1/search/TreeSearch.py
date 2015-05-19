import Node

def treeSearch(problem, fringe):
    solution = []
    root = Node.Node()
    root.state = problem.getStartState()
    
    fringe.push(root)
    while (not(fringe.isEmpty())):
        node = fringe.pop()
        if problem.isGoalState(node.state):
            current = node
            while (not(current.parent is None)):
                solution.append(current.action)
                current = current.parent
            solution.reverse()
            return solution
        else:
            for n in Node.expand(node, problem):
                fringe.push(n)
    return []
