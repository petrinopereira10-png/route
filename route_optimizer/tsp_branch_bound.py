
# TSP using Branch and Bound

def tsp_branch_and_bound(graph, start):
    n = len(graph)

    best_cost = float("inf")
    best_path = []

    visited = [False] * n
    path = [start]
    visited[start] = True

    def search(current, count, cost):
        nonlocal best_cost, best_path

        # Prune this route if it is already too expensive
        if cost >= best_cost:
            return

        # All cities visited: return to the starting city
        if count == n:
            if graph[current][start] > 0:
                total_cost = cost + graph[current][start]

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = path[:] + [start]

            return

        # Try each unvisited city
        for next_city in range(n):
            if not visited[next_city] and graph[current][next_city] > 0:
                visited[next_city] = True
                path.append(next_city)

                search(
                    next_city,
                    count + 1,
                    cost + graph[current][next_city]
                )

                path.pop()
                visited[next_city] = False

    search(start, 1, 0)

    return best_path, best_cost


# Test the algorithm
if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    cities = ["Depot", "A", "B", "C"]

    route, distance = tsp_branch_and_bound(graph, 0)

    if route:
        print("TSP using Branch and Bound")
        print("--------------------------------")
        print("Best route:", " -> ".join(cities[i] for i in route))
        print("Minimum distance:", distance)
    else:
        print("No complete round-trip route exists.")
