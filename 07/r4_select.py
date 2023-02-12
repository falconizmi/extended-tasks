from typing import Optional, List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional['Node'] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None


# Napište čistou funkci, která sestaví zřetězený seznam, který bude
# obsahovat hodnoty, které se nachází ve vstupním seznamu na
# zadaných indexech. Pořadí hodnot zachovejte. Předpokládejte, že
# indexy v seznamu ‹indices› jsou platné a vzestupně seřazené.

def select(indices: List[int], linked: LinkedList) -> LinkedList:
    result = LinkedList()
    idx_node = 0
    i = 0
    cur_node = linked.head
    cur_new_node = None
    while cur_node is not None and i < len(indices):

        if indices[i] == idx_node:
            assert cur_node is not None
            new_node = Node(cur_node.value)
            if result.head is None:
                result.head = new_node
                cur_new_node = result.head
            else:
                assert cur_new_node is not None
                cur_new_node.next = new_node
                cur_new_node = cur_new_node.next
            i += 1

        assert cur_node is not None
        cur_node = cur_node.next
        idx_node += 1

    return result


def main() -> None:
    assert select_test([], [], [])
    assert select_test([], [1, 2, 3], [])
    assert select_test([0, 2], [1, 2, 3], [1, 3])
    assert select_test([1], [1, 2, 3], [2])
    assert select_test([0, 1, 2], [1, 2, 3], [1, 2, 3])
    assert select_test([0, 2], [-1, -2, 3], [-1, 3])
    assert select_test([0, 2], [1, 2, 3], [1, 3])
    assert select_test([0, 3, 4], [0, 1, 2, 3, 4], [0, 3, 4])
    assert select_test([0, 1], [1, 2, 3], [1, 2])


def build_linked(nums: List[int]) -> LinkedList:
    result = LinkedList()

    if len(nums) == 0:
        return result

    result.head = Node(nums[0])
    tail = result.head

    for i in range(1, len(nums)):
        tail.next = Node(nums[i])
        tail = tail.next

    return result


def check_list_content(to_check: LinkedList,
                       expected_content: List[int]) -> bool:
    curr_idx = 0
    curr_node = to_check.head

    while curr_node is not None:
        if len(expected_content) == curr_idx:
            return False

        if curr_node.value != expected_content[curr_idx]:
            return False

        curr_node = curr_node.next
        curr_idx += 1

    return len(expected_content) == curr_idx


def select_test(chosen_idxs: List[int],
                list_nums: List[int],
                expected_content: List[int]) -> bool:
    test_list = build_linked(list_nums)
    select_res = select(chosen_idxs, test_list)

    if not check_list_content(test_list, list_nums):
        return False

    return check_list_content(select_res, expected_content)


if __name__ == "__main__":
    main()
