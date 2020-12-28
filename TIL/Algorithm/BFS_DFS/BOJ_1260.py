vertexList = ['0', '1', '2', '3', '4']
edgeList = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (3, 1),
            (3, 4), (4, 1), (4, 2), (4, 3)]
graphs = (vertexList, edgeList)


def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop(0)
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        if not current in visitedVertex:
            visitedVertex.append(current)
    return visitedVertex


print(dfs(graphs, 1))
