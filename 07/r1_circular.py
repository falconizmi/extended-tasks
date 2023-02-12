from typing import Optional, List


# V této úloze naprogramujeme lehce modifikovaný jednosměrně
# zřetězený seznam (ten standardní znáte z přednášky a z řešeného
# příkladu ‹sorted_list.py›). Rozdíl bude spočívat v tom, že
# poslední odkaz v seznamu nebude ‹None› jako dříve, ale bude
# ukazovat na hlavu, čím seznam uzavře do kruhu. Třída ‹Node›
# reprezentuje jeden uzel. Zvažte, jakého typu by měl být její
# atribut ‹next›.

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next = self


# Následuje třída ‹CircularList›, která má jediný povinný atribut,
# ‹head›, který ukazuje na hlavu seznamu. V prázdném seznamu by měla
# být v ‹head› uložena hodnota ‹None›. Hned po vytvoření
# reprezentuje instance třídy ‹CircularList› právě prázdný seznam.
# Naznačené metody nechť se chovají následovně:
#
#  • ‹insert› vloží novou hodnotu na začátek seznamu
#  • ‹last› vrátí poslední «uzel» (nikoliv hodnotu)
#
# Metody ‹split_by_value› a ‹split_by_node› rozdělí stávající seznam
# na dva kratší seznamy, a to tak, že uzly od hlavy až k uzlu
# popsaného parametrem (včetně) ponechá ve stávajícím seznamu, a ze
# zbytku vytvoří nový seznam, který vrátí. Pořadí uzlů (a tedy i
# hodnot) musí zůstat zachováno. Metoda ‹split_by_value› seznam
# rozdělí na prvním výskytu zadané hodnoty. Vstupní podmínky:
#
#  • hodnota předaná metodě ‹split_by_value› musí být v seznamu
#    aspoň jednou přítomna,
#  • uzel předaný metodě ‹split_by_node› patří tomuto seznamu.
#
# Příklad: uvažme hodnotu ‹lst› typu ‹CircularList›, která obsahuje
# prvky 4, 5, 1, 2, 3 a 7. Po provedení příkazu ‹new = lst.split(5)›
# zbudou v seznamu ‹lst› pouze hodnoty 4 a 5, zatímco seznam ‹new›
# bude mít prvky 1, 2, 3 a 7.

class CircularList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.last_node: Optional[Node] = None

    def insert(self, value: int) -> None:
        node: Node = Node(value)
        if self.head is None:
            self.head = node
            self.last_node = self.head
        else:
            next_node = self.head
            self.head = node
            node.next = next_node
            assert self.last_node is not None
            self.last_node.next = self.head

    def last(self) -> Optional[Node]:
        return self.last_node

    def split_by_value(self, value: int) -> 'CircularList':
        cur_node = self.head
        assert cur_node is not None
        ac_value: int = cur_node.value

        while ac_value != value:
            cur_node = cur_node.next
            ac_value = cur_node.value

        new_cir_lst = self.create_lst_from_split(cur_node.next)

        self.last_node = cur_node
        assert self.head is not None
        self.last_node.next = self.head

        return new_cir_lst

    def split_by_node(self, node: Node) -> 'CircularList':
        cur_node = self.head

        while cur_node != node:
            assert cur_node is not None
            cur_node = cur_node.next

        new_cir_lst = self.create_lst_from_split(cur_node.next)

        self.last_node = cur_node
        assert self.head is not None
        self.last_node.next = self.head

        return new_cir_lst

    def create_lst_from_split(self, start_node: Optional[Node]) -> 'CircularList':
        new_cir_lst = CircularList()
        cir_lst_values: List[int] = []
        while start_node != self.head:
            assert start_node is not None
            cir_lst_values.append(start_node.value)
            start_node = start_node.next

        for value in reversed(cir_lst_values):
            new_cir_lst.insert(value)

        return new_cir_lst


def main() -> None:
    test_init()
    test_last()
    test_split_by_node()
    test_split_by_value()


def test_split_by_value() -> None:
    c_list = make_list([4, 3, 2, 1])
    new = c_list.split_by_value(3)
    assert c_list.head is not None
    assert c_list.head.value == 4
    assert c_list.head.next is not None
    assert c_list.head.next.value == 3
    assert c_list.head.next.next is c_list.head

    assert new.head is not None
    assert new.head.value == 2
    assert new.head.next is not None
    assert new.head.next.value == 1
    assert new.head.next.next is new.head


def test_split_by_node() -> None:
    c_list = make_list([1, 2, 3, 4])
    assert c_list.head is not None
    new = c_list.split_by_node(c_list.head.next)

    assert c_list.head is not None
    assert c_list.head.value == 1
    assert c_list.head.next.value == 2
    assert c_list.head.next.next is c_list.head

    assert new.head is not None
    assert new.head.value == 3
    assert new.head.next.value == 4
    assert new.head.next.next is new.head


def test_last() -> None:
    c_list = CircularList()
    assert c_list.head is None
    assert c_list.last() is None

    c_list = make_list([-2])
    assert c_list.head is c_list.last()

    c_list = make_list([4, 2, 3, 1])
    node = c_list.last()
    assert node is not None
    assert c_list.head is node.next
    assert node.value == 1


def test_init() -> None:
    c_list = make_list([-2])
    assert c_list.head is not None
    assert c_list.head is c_list.head.next
    assert c_list.head.value == -2

    c_list = make_list([4, 2, 3, 1])
    assert c_list.head is not None
    assert c_list.head.value == 4
    assert c_list.head.next.value == 2
    assert c_list.head.next.next.value == 3
    assert c_list.head.next.next.next.value == 1
    assert c_list.head.next.next.next.next is c_list.head


def make_list(values: List[int]) -> CircularList:
    lst = CircularList()
    for value in reversed(values):
        lst.insert(value)
    return lst


if __name__ == "__main__":
    main()
