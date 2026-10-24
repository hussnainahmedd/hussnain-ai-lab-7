# 242816_Task1.py - CS344L Lab 7, Task 1: Minimax on a deeper tree
# Roll No: 242816 | Four levels: ROOT (MAX) -> A, B (MIN) -> A1..B2 (MAX) -> leaves
# Plain Python only. Run: python3 242816_Task1.py

TREE = {
    "ROOT": ["A", "B"],
    "A":  ["A1", "A2"],      "B":  ["B1", "B2"],
    "A1": ["a", "b"],        "A2": ["c", "d"],
    "B1": ["e", "f"],        "B2": ["g", "h"],
}

LEAF_VALUE = {
    "a": 5, "b": 6, "c": 7, "d": 4,
    "e": 5, "f": 3, "g": 6, "h": 6,
}

# The six parts of a game, as they appear in this tree (in my own words):
#   1. Initial state : ROOT, the node where the game starts.
#   2. Players       : MAX, who wants the biggest value, and MIN, who wants the smallest.
#   3. Actions       : the children of a node, given by TREE[node].
#   4. Result        : moving from a node down to one of its children.
#   5. Terminal test : a node with no entry in TREE is a leaf, so the game ends there.
#   6. Utility       : the leaf's number in LEAF_VALUE (good for MAX, bad for MIN).


def actions(node):
    """Return the children of a node; an empty list means it is a leaf."""
    return TREE.get(node, [])


def is_terminal(node):
    """Return True when a node has no entry in TREE, i.e. it is a leaf."""
    return node not in TREE


def utility(node):
    """Return the value of a leaf from LEAF_VALUE."""
    return LEAF_VALUE[node]


def minimax(node, maximising, counter, values):
    """Return the value of a node, store EVERY node's value in values, count visits."""
    counter[0] += 1
    if is_terminal(node):
        values[node] = utility(node)
        return values[node]
    if maximising:
        best = max(minimax(child, False, counter, values) for child in actions(node))
    else:
        best = min(minimax(child, True, counter, values) for child in actions(node))
    values[node] = best
    return best


def print_tree(node, depth, values):
    """Print the tree indented by depth, with each node's value and its role."""
    if is_terminal(node):
        role = "leaf"
    elif depth % 2 == 0:
        role = "MAX"
    else:
        role = "MIN"
    print("   " * (depth + 1) + f"{node} = {values[node]}  ({role})")
    for child in actions(node):
        print_tree(child, depth + 1, values)


def main():
    """Run minimax from ROOT and print the tree, the game value and MAX's move."""
    counter = [0]
    values = {}
    game_value = minimax("ROOT", True, counter, values)

    print("EVERY NODE'S VALUE")
    print_tree("ROOT", 0, values)
    print()
    print(f"   value of the game : {game_value}")
    print(f"   nodes visited     : {counter[0]}")
    print()
    print("WHICH MOVE SHOULD MAX PLAY?")
    for move in actions("ROOT"):
        print(f"   {move} = {values[move]}")
    best_move = max(actions("ROOT"), key=lambda m: values[m])
    print(f"   MAX plays {best_move}")


if __name__ == "__main__":
    main()
