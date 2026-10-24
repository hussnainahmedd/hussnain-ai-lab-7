# 242816_Task3.py - CS344L Lab 7, Task 3: Nim, a game you can actually win
# Roll No: 242816 | START = 7 + (242816 mod 6) = 7 + 2 = 9 stones.
# Rules: one pile, players take turns removing 1, 2 or 3 stones;
# the player who takes the LAST stone wins.
# Plain Python only. Run: python3 242816_Task3.py

START = 7 + (242816 % 6)  # 9 stones, from my own roll number

# The six parts of the game Nim:
#   1. Initial state : START stones in the pile.
#   2. Players       : MAX (moves first) and MIN, taking turns.
#   3. Actions       : take 1, 2 or 3 stones, never more than the pile holds.
#   4. Result        : the pile after the take, stones - take.
#   5. Terminal test : the pile is empty (0 stones).
#   6. Utility       : at an empty pile the player to move has LOST, so the
#      value is -1 when it is MAX's turn and +1 when it is MIN's turn.


def initial_state():
    """Return the starting pile size."""
    return START


def actions(stones):
    """Return the legal takes from this pile (1, 2 or 3, not more than stones)."""
    return [take for take in (1, 2, 3) if take <= stones]


def result(stones, take):
    """Return the pile left after taking stones."""
    return stones - take


def is_terminal(stones):
    """Return True when the pile is empty and nobody can move."""
    return stones == 0


def utility(stones, maximising):
    """Return the value of an empty pile: -1 if MAX to move, +1 if MIN to move."""
    return -1 if maximising else 1


def to_move(maximising):
    """Return the name of the player whose turn it is."""
    return "MAX" if maximising else "MIN"


def minimax(stones, maximising, counter):
    """Return +1 when MAX wins from this pile, -1 when MAX loses; count nodes."""
    counter[0] += 1
    if is_terminal(stones):
        return utility(stones, maximising)
    if maximising:
        return max(minimax(result(stones, take), False, counter)
                   for take in actions(stones))
    return min(minimax(result(stones, take), True, counter)
               for take in actions(stones))


def winning_take(stones):
    """Return one winning take for the player to move, or None if there is none."""
    for take in actions(stones):
        # A take wins when the opponent, now to move, loses from the new pile.
        if minimax(result(stones, take), False, [0]) == 1:
            return take
    return None


def main():
    """Score every first move from START, then tabulate every pile size 0 to 12."""
    pile = initial_state()
    counter = [0]
    scores = {}
    for take in actions(pile):
        scores[take] = minimax(result(pile, take), False, counter)

    print(f"From {pile} stones, each first move is worth:")
    for take in actions(pile):
        left = result(pile, take)
        outcome = "MAX wins" if scores[take] == 1 else "MAX loses"
        print(f"   take {take} -> {left} left : {scores[take]:+d}  ({outcome})")
    print()
    winning = [take for take in actions(pile) if scores[take] == 1]
    print(f"   winning first moves: {winning}")
    print(f"   nodes examined     : {counter[0]}")
    print()
    print("EVERY PILE SIZE FROM 0 TO 12")
    print("   stones   value for the player to move   winning take")
    for stones in range(13):
        take = winning_take(stones)
        if take is None:
            print(f"   {stones:<8} -1 (loses)                     -")
        else:
            print(f"   {stones:<8} +1 (wins)                      {take}")


if __name__ == "__main__":
    main()
