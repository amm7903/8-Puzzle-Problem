from cosc343EightPuzzle import EightPuzzle

puzzle = EightPuzzle(mode='hard')
init_state = puzzle.reset()


# definition of class named "Node"
class Node:
    def __init__(self, s, parent=None, g=0, h=0, action=None):
        self.s = s  # State
        self.parent = parent # Reference to parent node
        self.g = g # Cost
        self.f = g+h # evaluation function
        self.action = action # Nodes state to this node's state

# Function computing misplaced tiles
def heuristic(s, goal):
    man_dis = 0
    for (i, element) in enumerate(s):
        man_dis += abs(goal[i] % 3 - (element % 3)) + abs(goal[i] // 3 - (element // 3))
    return man_dis
    # h = 0
    # for i in range(len(s)):
    #     if s[i] != goal[i]:
    #         h += 1
    # return h

goal_state = puzzle.goal()
root_node = Node(s=init_state,parent=None, g=0, h=heuristic(s=init_state, goal=goal_state))
fringe = [root_node]
all_states = []

solution_node = None
while len(fringe)>0:
    current_node = fringe.pop(0)
    current_state = current_node.s
    if (current_state == goal_state):
        solution_node = current_node
        break
    else:
        available_actions = puzzle.actions(s=current_state)
        for a in available_actions:
            next_state = puzzle.step(s=current_state, a=a)
            new_node =Node(s=next_state,
                           parent=current_node,
                           g=current_node.g+1,
                           h=heuristic(s=next_state, goal=goal_state),
                           action=a)
            if new_node.s in all_states:
                pass
            else:
                fringe.append(new_node)
                all_states.append(new_node.s)
        fringe.sort(key=lambda x: x.f)

if solution_node is None:
        print("Didn't find a solution!!!")
else:

    action_sequence = []

    next_node = solution_node
    while True:
        if next_node == root_node:
            break

        action_sequence.append(next_node.action)
        next_node = next_node.parent

    action_sequence.reverse()
    print("Number of moves: %d" % solution_node.g)

    puzzle.show(s=init_state, a=action_sequence)

