from typing import List, Optional


# Implementujte funkci ‹left_bound›, která ve vzestupně seřazeném
# seznamu ‹values› co nejefektivněji najde index prvního výskytu
# hodnoty ‹target›. Pokud se hodnota v seznamu nenachází, vrátí
# ‹None›.

def left_bound(values: List[int], target: int) -> Optional[int]:
    low = 0
    high = len(values)
    while low < high:
        mid = (low + high) // 2
        if values[mid] > target:
            high = mid
        elif values[mid] < target:
            low = mid + 1
        elif mid == 0 or values[mid-1] < values[mid]:
            return mid
        else:
            high = mid
    return None


def main() -> None:
    assert left_bound([1, 2, 3, 4, 5], 2) == 1
    assert left_bound([1, 2, 2, 2, 2], 2) == 1
    assert left_bound([2, 2, 2, 2, 2], 2) == 0
    assert left_bound([2, 2, 2, 2, 3], 2) == 0
    assert left_bound([1, 2, 3, 4, 5], 7) is None


if __name__ == "__main__":
    main()
