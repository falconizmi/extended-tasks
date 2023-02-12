from typing import Optional, Tuple
from math import isclose


class Tree:
    def __init__(self, left: Optional['Tree'] = None,
                 right: Optional['Tree'] = None) -> None:
        self.left = left
        self.right = right


# Napište čistou funkci, která pro vstupní binární strom spočítá
# průměrnou délku větve (cesty od kořene k listu).

def average_branch_len(tree: Optional[Tree]) -> float:
    if tree is None:
        return 0
    length, ends = rec_count_brounch(tree)
    return length/ends


def rec_count_brounch(tree: Optional[Tree]) -> Tuple[float, float]:
    if tree is None:
        return (0,0)
    if tree.left is None and tree.right is None:
        return (1,1)
    if tree.left is None:
        length, ends = rec_count_brounch(tree.right)
        return length + ends, ends
    if tree.right is None:
        length, ends = rec_count_brounch(tree.left)
        return length + ends, ends

    l1, e1 = rec_count_brounch(tree.left)
    l2, e2 = rec_count_brounch(tree.right)
    if l1 == l2 and e1 == e2:
        return l1 + e1, e1
    return l1 + l2 + e1 + e2, e1 + e2


def main() -> None:
    assert isclose(average_branch_len(None), 0)
    assert isclose(average_branch_len(Tree()), 1)
    assert isclose(average_branch_len(Tree(Tree())), 2)
    assert isclose(average_branch_len(Tree(Tree(), Tree())), 2)
    assert isclose(average_branch_len(
        Tree(Tree(Tree()), Tree(Tree(), Tree(Tree())))), 10 / 3)
    assert isclose(average_branch_len(
        Tree(Tree(Tree(), Tree()),
             Tree(Tree(Tree(), Tree()),
                  Tree(Tree(Tree(), Tree()), Tree())))), 28 / 7)
    assert isclose(average_branch_len(
        Tree(None, Tree(Tree(None, Tree(
            Tree(None, Tree()), None)), None))), 6)
    assert isclose(average_branch_len(
        Tree(Tree(Tree(Tree())), Tree())), 3)
    assert isclose(average_branch_len(
        Tree(Tree(Tree(Tree(Tree()))), Tree())), 7 / 2)


if __name__ == "__main__":
    main()
