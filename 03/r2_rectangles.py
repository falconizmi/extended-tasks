# Napište (čistou) funkci, která jako parametr dostane seznam
# obdélníků a vrátí seznam obdélníků, které se překrývají s nějakým
# jiným. Obdélník samotný je reprezentovaný dvěma body (levým dolním
# a pravým horním rohem, a má nenulovou výšku i šířku). Obdélníky
# budeme zapisovat jako dvojice dvojic – ‹((0, 0), (1, 2))›
# například reprezentuje tento obdélník:
#
#           ┌───┐(1, 2)
#           │   │
#           │   │
#     (0, 0)└───┘
#
# Mohl by se Vám hodit predikát, který je pravdivý, když se dva
# obdélníky překrývají:

def has_overlap(a, b):
    a1, a2 = a
    a1_x, a1_y = a1
    a2_x, a2_y = a2

    b1, b2 = b
    b1_x, b1_y = b1
    b2_x, b2_y = b2

    x_pos = (a1_x <= b1_x and b1_x <= a2_x or
             a1_x <= b2_x and b2_x <= a2_x )

    y_pos = (a1_y <= b1_y and b1_y <= a2_y or
             a1_y <= b2_y and b2_y <= a2_y)

    return x_pos and y_pos

def filter_overlapping(rectangles):
    result = []
    for i, r1 in enumerate(rectangles):
        for j, r2 in enumerate(rectangles):
            if i != j and has_overlap(r1, r2):
                result.append(r1)
                break
    return result


def main():
    r1 = ((1, 1), (2, 2))
    r2 = ((0, 0), (2, 2))
    r3 = ((-2, -2), (-1, -1))
    r4 = ((10, 15), (25, 35))

    assert filter_overlapping([]) == []
    assert filter_overlapping([r1]) == []
    assert filter_overlapping([r1, r1]) == [r1, r1]
    assert filter_overlapping([r1, r2]) == [r1, r2]
    assert filter_overlapping([r2, r1]) == [r2, r1]

    assert filter_overlapping([r3, r2, r1, r4]) == [r2, r1]
    assert filter_overlapping([r2, ((1, 10), (10, 20))]) == []
    assert filter_overlapping([((15, 0), (17, 8)),
                               ((1, 10), (10, 20))]) == []
    l2 = [((0, 0), (2, 2)),
          ((1, 1), (10, 10)),
          ((9, 9), (11, 11))]
    assert filter_overlapping(l2) == l2


if __name__ == "__main__":
    main()
