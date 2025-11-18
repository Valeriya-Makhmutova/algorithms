import heapq

n, m, s, t, C = map(int, input().split())
list_ = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, time, cost = map(int, input().split())
    list_[u].append((v, time, cost))

max_limit = 10**6
dist = [dict() for _ in range(n + 1)]
dist[s][0] = 0

pq = [(0, 0, s)]

while pq:
    time_now, cost_now, u = heapq.heappop(pq)
    if cost_now in dist[u] and dist[u][cost_now] < time_now:
        continue
    for v, time_edge, cost_edge in list_[u]:
        new_cost = cost_now + cost_edge
        if new_cost > C:
            continue
        new_time = time_now + time_edge

        if any(c <= new_cost and dist[v][c] <= new_time for c in dist[v]):
            continue

        dist[v][new_cost] = new_time
        heapq.heappush(pq, (new_time, new_cost, v))

result = min(dist[t].values(), default=max_limit)

if result != max_limit:
    print(result)
else:
    print(-1)