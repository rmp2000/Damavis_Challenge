from collections import defaultdict, deque
from Challenge import *
def bfs(lab, start):
    end= [len(lab)-1,len(lab[len(lab)-1])-1]
    visited = []
    queue = deque([(start, 0)])
    visited.append(start)

    while queue:
        vertex, steps = queue.popleft()
        if vertex[2]==end:
            return steps
        
        for i in range(5):
            match i:
                case 0:
                    neighbor = move_right(vertex,lab)
                    if neighbor==-1:
                        continue
                case 1:
                    neighbor = move_left(vertex,lab)
                    if neighbor==-1:
                        continue
                case 2:
                    neighbor = move_down(vertex,lab)
                    if neighbor==-1:
                        continue
                case 3:
                    neighbor = move_up(vertex,lab)
                    if neighbor==-1:
                        continue
                case 4:
                    neighbor = rotar(vertex,lab)
                    if neighbor==-1:
                        continue

            if neighbor not in visited:
                queue.append((neighbor, steps + 1)) 
                visited.append(neighbor)  
    return -1
