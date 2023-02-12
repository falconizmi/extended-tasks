from typing import Set


# Napište čistou funkci, která vrátí množinu všech slov, tvořených
# znaky ‹{"0", "1", "2"}› s danou délkou ‹length› a váhou ‹weight›.
# Váhou myslíme počet nenulových číslic v daném slově.

def weighted_words(length: int, weight: int) -> Set[str]:
    result: Set[str] = set()
    rec_weighted_words(length, 0, weight, "", result)
    return result


def rec_weighted_words(length: int, cur_len: int, weight: int, cur_word: str, result: Set[str]) -> None:
    if len(cur_word) == length:
        result.add(cur_word)
        return

    if length - cur_len == 0 or length - cur_len < weight:
        return

    if length - cur_len > weight:
        rec_weighted_words(length, cur_len+1, weight, cur_word + "0", result)

    if weight > 0:
        for n in "12":
            rec_weighted_words(length, cur_len+1, weight-1, cur_word + n, result)


def main() -> None:
    assert weighted_words(1, 2) == set()
    assert weighted_words(0, 0) == {""}
    assert weighted_words(2, 2) == {"11", "12", "21", "22"}
    assert weighted_words(3, 1) == {"001", "002", "010", "020", "100", "200"}


if __name__ == '__main__':
    main()
