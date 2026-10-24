# CS344L Lab 7 — Adversarial Search

**Student:** Hussnain Ahmad · **Roll No:** 242816 · **Course:** CS344L Artificial Intelligence Lab, Air University Islamabad

Three Python files, one per task. Plain Python only — nothing to install. Every file runs on its own and prints exactly what the task sheet asks for. All code is written from scratch (the lecture's eight part files were reference only); every function carries a short comment explaining what it does.

## How to run

```bash
python3 242816_Task1.py
python3 242816_Task2.py
python3 242816_Task3.py
```

## Task 1 — Minimax on a deeper tree

A four-level tree (ROOT = MAX, A/B = MIN, A1–B2 = MAX, eight leaves) with minimax alternating max/min at every level. The program prints every node's value with its role, the value of the game, the node count, and MAX's move.

**Result:** value of the game = **6**, nodes visited = **15**, MAX plays **A** (A = 6, B = 5).

## Task 2 — Alpha-beta pruning

The same tree and values as Task 1, with alpha-beta pruning added. Every cut-off is printed with the node and the alpha/beta values that caused it, and a `seen` set works out which nodes were never examined.

**Result:** same value **6**, nodes visited = **11** (4 saved), cut-offs = **2** (at A2: alpha 7 ≥ beta 6; at B: alpha 6 ≥ beta 5). Never examined: **d, B2, g, h**.

## Task 3 — Nim, a game you can actually win

One pile, players take 1–3 stones, last stone wins. Starting pile from my own roll number: **START = 7 + (242816 mod 6) = 9 stones**. The utility is the tricky part: at an empty pile the player to move has lost, so it returns −1 on MAX's turn and +1 on MIN's turn.

**Result:** from 9 stones, take **1** is the only winning first move (leaves 8, a losing pile for the opponent). Pile sizes 0–12: the player to move loses exactly on **0, 4, 8, 12** — every multiple of 4. Winning strategy: **always leave a multiple of 4**.

## Files

| File | Task |
|---|---|
| `242816_Task1.py` | Minimax on the four-level tree |
| `242816_Task2.py` | Minimax + alpha-beta pruning, comparison table |
| `242816_Task3.py` | Nim from 9 stones + pile-size table 0–12 |
| `screenshots/` | Terminal output screenshots for all three tasks |
