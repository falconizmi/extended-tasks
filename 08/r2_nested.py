from typing import List


# Implementujte čistou funkci ‹sort_nested›, která vzestupně
# uspořádá prvky v seznamu seznamů čísel ‹lists›, a to tak, že
# přeuspořádá jenom čísla ve vnitřních seznamech, aniž by měnil
# jejich délku. Výstupní seznam bude tedy obsahovat stejný počet
# stejně dlouhých seznamů jako ten vstupní, ale v obecném případě
# budou tyto vnořené seznamy obsahovat jiná čísla.

def sort_nested(lists: List[List[int]]) -> List[List[int]]:
    flatted_lst = []
    for l in lists:
        for v in l:
            flatted_lst.append(v)
    flatted_lst.sort()

    result: List[List[int]] = []
    idx = 0
    for i in range(len(lists)):
        result.append([])
        for _ in range(len(lists[i])):
            result[i].append(flatted_lst[idx])
            idx += 1
    return result


def main() -> None:
    assert sort_nested([[5, 4], [1, 2, 3]]) == [[1, 2], [3, 4, 5]]
    assert sort_nested([[5], [4], [1, 2, 3]]) == [[1], [2], [3, 4, 5]]
    assert sort_nested([[5], [4], [2, 1], [3]]) == [[1], [2], [3, 4], [5]]
    assert sort_nested([[5], [4, 2, 1], [3]]) == [[1], [2, 3, 4], [5]]
    lists = [[5], [4, 2, 1], [3]]
    assert sort_nested(lists) == [[1], [2, 3, 4], [5]]
    assert lists == [[5], [4, 2, 1], [3]]


if __name__ == "__main__":
    main()
