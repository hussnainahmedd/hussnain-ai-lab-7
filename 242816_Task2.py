# 242816_Task2.py - CS344L Lab 7, Task 2: Minimax + alpha-beta pruning
# Roll No: 242816 | Same tree, same leaf values and same answer as Task 1;
# only the amount of work changes, because alpha-beta prunes branches.
# Plain Python only. Run: python3 242816_Task2.py

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

# Nodes in depth-first order, so "never examined" reads like the tree itself.
ALL_NODES = ["ROOT", "A", "A1", "a", "b", "A2", "c", "d",
             "B", "B1", "e", "f", "B2", "g", "h"]


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
    """Plain minimax from Task 1: value of a node, all values stored, visits counted."""
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


def alphabeta(node, alpha, beta, maximising, counter, seen, cuts):
    """Return the value of a node with alpha-beta pruning, recording every node touched."""
    counter[0] += 1
    seen.add(node)
    if is_terminal(node):
        return utility(node)
    if maximising:
        value = float("-inf")
        for child in actions(node):
            value = max(value, alphabeta(child, alpha, beta, False, counter, seen, cuts))
            alpha = max(alpha, value)
            if alpha >= beta:  # MIN above will never let this branch be chosen
                print(f"      CUT at {node}: alpha {alpha} >= beta {beta}")
                cuts[0] += 1
                break
        return value
    value = float("inf")
    for child in actions(node):
        value = min(value, alphabeta(child, alpha, beta, True, counter, seen, cuts))
        beta = min(beta, value)
        if alpha >= beta:  # MAX above already has something at least this good
            print(f"      CUT at {node}: alpha {alpha} >= beta {beta}")
            cuts[0] += 1
            break
    return value


def main():
    """Run minimax, then alpha-beta, and compare the two runs."""
    # Plain minimax run (same as Task 1, for the comparison table).
    mm_counter = [0]
    mm_values = {}
    mm_value = minimax("ROOT", True, mm_counter, mm_values)

    # Alpha-beta run, starting with the widest possible window.
    print("ALPHA-BETA RUN")
    ab_counter = [0]
    seen = set()
    cuts = [0]
    ab_value = alphabeta("ROOT", float("-inf"), float("inf"), True,
                         ab_counter, seen, cuts)
    print()
    print("COMPARISON")
    print("   algorithm       value   nodes   cuts")
    print(f"   minimax         {mm_value}       {mm_counter[0]}      -")
    print(f"   alpha-beta      {ab_value}       {ab_counter[0]}      {cuts[0]}")
    print()
    print(f"   same value: {mm_value == ab_value}")
    print(f"   nodes saved: {mm_counter[0] - ab_counter[0]}")
    print()
    skipped = [node for node in ALL_NODES if node not in seen]
    print(f"NEVER EXAMINED: {skipped}")
    for node in skipped:
        if is_terminal(node):
            print(f"   {node} = {LEAF_VALUE[node]}  (leaf, skipped)")


if __name__ == "__main__":
    main()
