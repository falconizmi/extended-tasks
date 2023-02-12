from typing import Optional


# † Naprogramujte datovou strukturu ‘zipper’: jedná se o strukturu
# podobnou zřetězenému seznamu, s jedním důležitým rozdílem: přesto,
# že používá jednoduché zřetězení (nikoliv dvojité), lze se v něm
# efektivně pohybovat oběma směry. Nicméně na rozdíl od dvojitě
# zřetězeného seznamu nám zipper umožňuje udržovat pouze jediný
# kurzor.
#
# Jak zipper funguje? Používá následující strukturu:
#
#  ┌───────────┐  ┌───┐  ┌────────┐  ┌───┐  ┌────────────┐
#  │ left tail │◀─│ … │◀─│ cursor │─▶│ … │─▶│ right tail │
#  └───────────┘  └───┘  └────────┘  └───┘  └────────────┘
#
# Jak efektivně kurzor posunout o jednu pozici doleva nebo doprava
# si pravděpodobně dovedete představit. Pro jednoduchost budeme
# uvažovat pouze neprázdný zipper.
#
# Pro zajímavost: zipper lze implementovat také pomocí dvojice
# zásobníků, a tato implementace je typicky efektivnější. V tomto
# cvičení ale preferujeme použití zřetězených struktur.


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional['Node'] = None


class Zipper:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    # Vrátí aktuální hodnotu kurzoru.

    def cursor(self) -> int:
        return self.value

    # Vloží prvek nalevo od kurzoru.

    def insert_left(self, num: int) -> None:
        node = Node(num)
        if self.left is None:
            self.left = node

        else:
            cur_left = self.left
            self.left = node
            self.left.next = cur_left

    # Smaže prvek nalevo od kurzoru, existuje-li takový, a vrátí
    # jeho hodnotu. Jinak vrátí ‹None›.

    def delete_left(self) -> Optional[int]:
        if self.left is None:
            return None
        node = self.left
        self.left = self.left.next
        return node.value

    # Posune kurzor o jednu pozici doleva.

    def shift_left(self) -> None:
        if self.left is not None:
            self.value, self.left.value = self.left.value, self.value
            new_left = self.left.next
            self.left.next = self.right
            self.right = self.left
            self.left = new_left

    # Posune kurzor o jednu pozici doprava.

    def shift_right(self) -> None:
        if self.right is not None:
            self.value, self.right.value = self.right.value, self.value
            new_right = self.right.next
            self.right.next = self.left
            self.left = self.right
            self.right = new_right


def main() -> None:
    zipper = Zipper(1)  # [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() is None
    zipper.insert_left(1)  # 1 [1]
    zipper.insert_left(2)  # 1 2 [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() == 2  # 1 [1]
    zipper.insert_left(3)  # 1 3 [1]
    zipper.insert_left(3)  # 1 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_left()    # 1 3 [3] 1
    zipper.shift_right()   # 1 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_left()   # 1 3 [3] 1
    assert zipper.delete_left() == 3  # 1 [3] 1
    assert zipper.delete_left() == 1  # [3] 1
    assert zipper.cursor() == 3
    zipper.insert_left(2)  # 2 [3] 1
    zipper.insert_left(3)  # 2 3 [3] 1
    assert zipper.cursor() == 3
    zipper.shift_right()  # 2 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_right()  # no change
    assert zipper.cursor() == 1
    zipper.shift_left()  # 2 3 [3] 1
    assert zipper.cursor() == 3
    assert zipper.delete_left() == 3  # 2 [3] 1
    zipper.shift_left()  # [2] 3 1
    assert zipper.delete_left() is None
    zipper.shift_right()  # 2 [3] 1
    assert zipper.cursor() == 3
    assert zipper.delete_left() == 2
    zipper.shift_right()  # 3 [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() == 3
    assert zipper.delete_left() is None
    zipper.shift_right()
    assert zipper.cursor() == 1
    assert zipper.delete_left() is None


if __name__ == '__main__':
    main()
