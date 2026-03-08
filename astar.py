import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor)
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None


graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',1)],
    'C':[('D',1)],
    'D':[('E',2)],
    'E':[]
}

heuristic = lambda x: 1

print(a_star(graph,'B','E',heuristic))