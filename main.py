# визначення функції для знаходження кореня дерева
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# функція для злиття двох множин
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # приєднати менше дерево до більшого та оновити ранги
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# функція для виконання алгоритму Крускала
def kruskalMST(graph):
    V = len(graph)

    # сортування ребер у порядку зростання ваги
    edges = []
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] != 0:
                edges.append([graph[i][j], i, j])
    edges.sort()

    # збереження ребер, що входять до остового дерева
    result = []
    parent = []
    rank = []

    # створення окремої множини для кожної вершини
    for node in range(V):
        parent.append(node)
        rank.append(0)

    i = 0
    e = 0

    # додавання ребер до остового дерева, поки кількість ребер не дорівнює V-1
    while e < V - 1:
        w, u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # додавання ребра до результату, якщо воно не створює цикл
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    # виведення результату
    print("Кількість вершин: ", V)
    print("Матриця ваг: ")
    for row in graph:
        print(row)

    print("\nМінімальне остове дерево: ")
    for u, v, weight in result:
        print("%d - %d: %d" % (u, v, weight))

    print("\nСумарна вага: ", sum(weight for u, v, weight in result))


# задана матриця суміжності
graph = [
    [0, 0, 38, 95, 0, 1, 57, 0],
    [0, 0, 0, 0, 79, 0, 36, 19],
    [38, 0, 0, 51, 0, 0, 44, 0],
    [95, 0, 51, 0, 0, 44, 0, 0],
    [0, 79, 0, 0, 0, 93, 41, 48],
    [1, 0, 0, 44, 93, 0, 1, 0],
    [57, 36, 44, 0, 41, 1, 0, 0],
    [0, 19, 0, 0, 48, 0, 0, 0]
]

kruskalMST(graph)
