from collections import deque, defaultdict
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = dict()
        # need to find the "out-graph" before proceeding
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)

                # set in-degree count dictionary
                in_degree[recipe] = in_degree.get(recipe, 0) + 1
                if ingredient not in in_degree:
                    in_degree[ingredient] = 0

        stash = set(supplies)
        queue = deque([k for k, v in in_degree.items() if v == 0 and k in stash])
        while len(queue):
            food = queue.popleft()
            stash.add(food)
            for child in graph[food]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return [r for r in recipes if r in stash]
