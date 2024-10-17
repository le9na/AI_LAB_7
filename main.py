class Greedy:
    def __init__(self):
        self.N = 12  # updated number of vertices in the graph
        self.G = [[False] * self.N for _ in range(self.N)]  # adjacency matrix
        self.StrdestToGoal = [0] * self.N  # distances to goal
        self.path = []  # to store the path taken

        self.setup_graph()
        self.setup_strdest()

        print("------------------------------\n")
        self.greedy(0)
        print("\n------------------------------\n")
        print("Path taken: " + " ".join(self.path))

    def setup_graph(self):
        edges = [
            (0, 1),
            (0, 8),
            (0, 4),
            (1, 2),
            (1, 3),
            (2, 6),
            (3, 4),
            (3, 5),
            (6, 7),
            (8, 9),
            (9, 10),
            (10, 11)
        ]
        for (i, j) in edges:
            self.G[i][j] = self.G[j][i] = True

    def setup_strdest(self):
        self.StrdestToGoal = [
            86,
            59,
            164,
            29,
            28,
            0,
            109,
            239,
            44,
            52,
            68,
            74
        ]

    def h_func(self, i):
        return self.StrdestToGoal[i]

    def greedy(self, loc):
        self.path.append(self.ret_city(loc))
        if self.h_func(loc) == 0:
            print("Goal has been reached, at AlRass now")
            return

        print(f"The current location is: {self.ret_city(loc)} (its distance to the goal: {self.h_func(loc)})")

        neighbors = []
        print("[", end="")
        for i in range(self.N):
            if self.G[i][loc]:
                neighbors.append(i)
                print(f"{self.ret_city(i)}({self.h_func(i)})", end=" ")
        print("]\n")

        if len(neighbors) == 1:
            self.greedy(neighbors[0])
            return

        # Choose the neighbor with the smallest heuristic value
        dest = min(neighbors, key=self.h_func)
        self.greedy(dest)

    @staticmethod
    def ret_city(i):
        cities = [
            "Buraydah", # 86
            "Unayzah", # 59
            "AlZulfi", # 164
            "Al-Badai", # 29
            "Riyadh-Alkhabra", # 28
            "AlRass", # 0
            "UmSedrah", # 109
            "Shakra", # 239
            "Al-Bukayriyah", # 44
            "Sheehyah", # 52
            "Dhalfa", # 68
            "Mulida" # 74
        ]
        return cities[i]


# Run the Greedy search
greedy_search = Greedy()
