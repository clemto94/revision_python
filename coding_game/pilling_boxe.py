"""
Objective
Stack the boxes on the platform "A", in order of size (the biggest at the bottom).
Rules
You work in an automated factory that controls a robotic arm to move boxes. The boxes are positioned
in 3 stacks: "A", "B" and "C". The arm can move above each stack to pick or release a box. Your goal is to
rearrange the boxes to stack all of them onto the platform "A", in order of size. Your function is given 3
lists. Each list contains the size of every box in the corresponding stack (from bottom to top). To succeed,
your program must output the list of commands for the arm to execute. A command is composed of two
letters separated by a space: the source stack from which to pick a box, and the destination stack onto
which to drop the box. It is not necessary to minimize the number of commands but this number should
not exceed 200 .
Implementation Implement the function solve(boxes_a, boxes_b, boxes_c) which takes 3 arrays
of integers: boxes_a, boxes_b and boxes_c. The function must return a list of strings: the name of the
source stack and the name of the destination stack, separated by a space. For example, your function
may return the following list of actions "A C", "B C" and "A B" in order to move a box from A to C, then a
box from B to C and then a box from A to B.
Victory Conditions
All boxes are piled on stack A, in order of size.
Lose Conditions
Your program outputs an invalid command. Your program needs more than 200 commands.
Constraints
20 ≤ size ≤ 200
3 ≤ number of boxes ≤ 8
"""
import sys
from contextlib import redirect_stdout


def solve(boxes_a, boxes_b, boxes_c):
    stacks = {
        'A': boxes_a[:],
        'B': boxes_b[:],
        'C': boxes_c[:]
    }

    commands = []

    # Rassembler toutes les boîtes
    all_boxes = []
    for name in ['A', 'B', 'C']:
        for size in stacks[name]:
            all_boxes.append(size)

    # Trier du plus grand au plus petit
    all_boxes.sort(reverse=True)

    # Trouver dynamiquement où est chaque boîte
    def find_stack_containing(size):
        for name in ['A', 'B', 'C']:
            if size in stacks[name]:
                return name
        return None

    for size in all_boxes:
        current_stack = find_stack_containing(size)

        if current_stack is None:
            continue  # déjà déplacée

        # Dégager les boîtes au-dessus si nécessaire
        while stacks[current_stack][-1] != size:
            temp_dest = [s for s in 'ABC' if s != current_stack and s != 'A']
            for dest in temp_dest:
                if not stacks[dest] or stacks[dest][-1] > stacks[current_stack][-1]:
                    break
            else:
                raise ValueError("Aucune pile valide pour dégager temporairement.")

            top = stacks[current_stack].pop()
            stacks[dest].append(top)
            commands.append(f"{current_stack} {dest}")

        # Dégager pile A si son sommet est plus petit que size
        while stacks['A'] and stacks['A'][-1] < size:
            dest = [s for s in 'BC' if not stacks[s] or stacks[s][-1] > stacks['A'][-1]][0]
            top = stacks['A'].pop()
            stacks[dest].append(top)
            commands.append(f"A {dest}")

        # Déplacer la boîte vers A
        stacks[current_stack].pop()
        stacks['A'].append(size)
        commands.append(f"{current_stack} A")

    return commands


def main():
    # pylint: disable = C, W
    boxes_count_a = int(input())
    boxes_a = [int(i) for i in input().split()]
    boxes_count_b = int(input())
    boxes_b = [int(i) for i in input().split()]
    boxes_count_c = int(input())
    boxes_c = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        actions = solve(boxes_a, boxes_b, boxes_c)
        for i in range(len(actions)):
            print(actions[i])

if __name__ == "__main__":
    # main()
    cmds = solve([100], [80, 60], [90])
    print(cmds)
