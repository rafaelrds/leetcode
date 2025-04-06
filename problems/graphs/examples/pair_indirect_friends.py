# FIXME using blossom algorithm instead


class Solution:
    def pair_indirect_friends(self, graph):
        if not graph:
            raise ValueError("Graph should contain elements")
        if len(graph) % 2 != 0:
            raise ValueError("Cannot split an odd number of friends")

        self.res = []
        self.picked = set()

        def dfs(node, original, visited):
            if node in visited or node == original:
                return
            if original not in graph[node] and original not in self.picked:
                picked = tuple(sorted([original, node]))
                self.res.append(picked)
                self.picked.add(node)
                self.picked.add(original)
                return

            visited.add(node)

            for direct_friend in graph[node]:
                dfs(direct_friend, original, visited)

        # call dfs to fill response list
        for person in graph:
            for friend in graph[person]:
                dfs(friend, person, set())
        return self.res


if __name__ == "__main__":
    graph = {
        'alice': ['bob'],
        'bob': ['charlie', 'alice'],
        'charlie': ['bob', 'john'],
        'john': ['charlie'],
    }
    res = Solution().pair_indirect_friends(graph)
    print(res)
