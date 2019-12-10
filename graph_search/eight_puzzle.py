from collections import deque


def find_blank_location(state):
    idx = state.index('#')
    return idx//3, idx%3 
parent = {}
def bfs(begin, target):
    i, j = find_blank_location(begin) 
    open_queue = deque([(i, j, begin)])
    seen = {begin}
    while open_queue:
        i, j, state = open_queue.popleft()
        old_state = list(state)
        for di, dj in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
            r, c = i+di, j+dj
            if 0<=r<3 and 0<=c<3:
                new_state = old_state[:]
                new_state[3*r+c], new_state[3*i+j] = old_state[3*i+j],old_state[3*r+c]
                # a, b = b, a
                new_state = ''.join(new_state)
                if new_state not in seen:
                    parent[new_state] = state
                    if new_state == target:
                        print('Solution found!', new_state)
                        #print(parent)
                        #print("1423586#7" in parent)
                        #solution = []

                        #return []
                        current_node = new_state
                        solution = [current_node]
                        print(parent)
                        while current_node in parent:
                            parent_node = parent[current_node]
                            solution.append(parent_node)
                            current_node = parent_node
                            print(solution)
                        return solution[::-1]
                    open_queue.append((r, c, new_state))
                    seen.add(new_state)


def solve(begin, target):
    solution = bfs(begin, target)
    return solution
    #return solution


def print_solution(s):
    for i in range(3):
        print(s[i*3:i*3+3])
#begin = "31245678#"
begin = "1423586#7"
target = "#12345678"
solution = solve(begin, target)
print('We need ', len(solution), 'steps to find the solution')
for i,s in enumerate(solution):
    print('*********** step ', i, '  **************')
    print_solution(s)
