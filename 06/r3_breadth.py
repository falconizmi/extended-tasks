from typing import Dict, List

# Uvažujme neprázdný strom s očíslovanými vrcholy (kořen má vždy
# číslo 1), např.:
#
#             ┌───┐
#             │ 1 │
#             └───┘
#          ╭───╯ ╰────╮
#          ▼          ▼
#        ┌───┐      ┌───┐
#        │ 2 │      │ 3 │
#        └───┘      └───┘
#    ╭────╯│╰────╮    │
#    │     │     │    │
#    ▼     ▼     ▼    ▼
#  ┌───┐ ┌───┐ ┌───┐ ┌───┐
#  │ 4 │ │ 5 │ │ 6 │ │ 7 │
#  └───┘ └───┘ └───┘ └───┘
#
# Tento strom zakódujeme do slovníku takto:

Tree = Dict[int, List[int]]


def example_tree() -> Tree:
    return {1: [2, 3],
            2: [4, 5, 6],
            3: [7],
            4: [], 5: [], 6: [], 7: []}


# Tedy klíče jsou čísla vrcholů a hodnoty jsou seznamy jejich
# (přímých) potomků. Napište čistou funkci, která najde „nejdelší
# řádek“ v obrázku takovéhoto stromu. Řádek je vždy tvořen uzly,
# které mají stejnou vzdálenost od kořene.

# Pomůcka: máte-li uložený nějaký řádek v seznamu, lehce získáte
# řádek následující (o jedna vzdálenější od kořene). Pak už stačí
# nalézt nejdelší takový seznam.

def breadth(tree: Tree) -> int:
    lines = [[1]]
    i = 0
    while i < len(lines):
        line = []
        for e in lines[i]:
            for v in tree[e]:
                line.append(v)
        if len(line) != 0:
            lines.append(line)
        i += 1
    return max([len(lst) for lst in lines])



def main() -> None:
    assert breadth({1: []}) == 1
    assert breadth({1: [2], 2: []}) == 1
    assert breadth({1: [2], 2: [3, 4], 3: [], 4: []}) == 2

    assert breadth(example_tree()) == 4

    big_tree: Tree = {1: [2, 3, 4], 2: [], 3: [5, 6], 4: [7],
                      5: [8, 9, 10], 6: [11], 7: [], 8: [],
                      9: [12], 10: [], 11: [], 12: []}
    assert breadth(big_tree) == 4


if __name__ == "__main__":
    main()
