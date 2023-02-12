from typing import List

# Na vstupu dostanete neprázdný seznam čísel. Vaším úkolem je vrátit
# množinu všech seznamů, které:
#
#  1. jsou vlastními podposloupnostmi vstupního seznamu, tzn.
#     vzniknou ze vstupního seznamu vynecháním alespoň jednoho
#     prvku,
#  2. jsou neklesající, tzn. pro seznam ‹out› a celá čísla ‹i›, ‹j›
#     platí ‹i < j› → ‹out[i] ≤ out[j]›.
#
# Protože datový typ ‹set› neumožňuje ukládat seznamy jako prvky,
# výstup uložte do seznamu (na pořadí jednotlivých posloupností v
# tomto seznamu nezáleží).


def subseq(seq: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    rec_subseq(seq, [], [], result)
    result.append([])
    return result


def rec_subseq(seq: List[int], cur_seq: List[int],
               seq_idx: List[int], result: List[List[int]]) -> None:
    if len(cur_seq) + 1 >= len(seq):
        return

    for i, n in enumerate(seq):
        last_idx = None if len(seq_idx) == 0 else seq_idx[-1]
        if last_idx is None or (last_idx < i and seq[last_idx] <= n):
            new_seq = cur_seq + [n]
            if new_seq not in result:
                result.append(new_seq)
                rec_subseq(seq, new_seq, seq_idx + [i], result)

    return

def main() -> None:
    subseq_test([1], [[]])
    subseq_test([1, 2], [[], [1], [2]])
    subseq_test([2, 1], [[], [1], [2]])
    subseq_test([2, 2, 2], [[], [2], [2, 2]])
    subseq_test([2, 1, 2], [[], [1], [2], [2, 2], [1, 2]])
    subseq_test([-1, 0, 1], [[], [-1], [0], [1],
                             [-1, 0], [-1, 1], [0, 1]])
    subseq_test([1, -12, 0, 55], [[], [1], [-12],
                                  [0], [55], [1, 55],
                                  [-12, 0], [-12, 0, 55],
                                  [-12, 55], [0, 55]])
    subseq_test([3, 2, 1], [[], [3], [2], [1]])


def subseq_test(input_seq: List[int],
                expected: List[List[int]]) -> None:
    original_seq = input_seq.copy()
    result = subseq(input_seq)

    assert input_seq == original_seq

    result.sort()
    expected.sort()
    assert result == expected, (result, expected)


if __name__ == '__main__':
    main()
