# † Vaším úkolem je tentokrát naprogramovat tzv. „hru života“ –
# jednoduchý dvourozměrný celulární automat. Simulace běží na
# čtvercové síti, kde každá buňka je mrtvá (hodnota 0) nebo živá
# (hodnota 1). V každém kroku se přepočte hodnota všech buněk, a to
# podle toho, zda byly v předchozím kroku živé a kolik měly živých
# sousedů (z celkem osmi, tzn. včetně úhlopříčných):
#
# │  stav │ živí sousedé │ výsledek │
# ├───────┼──────────────┼──────────┤
# │  živá │          0–1 │    mrtvá │
# │  živá │          2–3 │     živá │
# │  živá │          4–8 │    mrtvá │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ mrtvá │          0–2 │    mrtvá │
# │ mrtvá │            3 │     živá │
# │ mrtvá │          4-8 │    mrtvá │

# Příklad krátkého výpočtu:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │ ○ │   │   │ → │ ○ │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Napište čistou funkci, která dostane jako parametry počáteční stav
# hry (jako dvourozměrný seznam nul a jedniček) a počet kroků a
# vrátí stav hry po odpovídajícím počtu kroků.

def life(initial, generations):
    previous = initial
    for _ in range(generations):
        new = copy_life(previous)
        for y in range(len(new)):
            for x in range(len(new[0])):
                set_life(x, y, new, previous)
        previous = new

    return previous


def copy_life(lst):
    result = []
    for i, l in enumerate(lst):
        result.append([])
        for e in l:
            result[i].append(e)
    return result


def set_life(x, y, new, previous):
    alive_neigh = 0
    for i in range(-1, 2):
        if y + i >= 0 and y + i < len(previous):
            for j in range(-1, 2):
                if x + j >= 0 and x + j < len(previous[0]):
                    if previous[y + i][x + j] == 1 and (j != 0 or i != 0):
                        alive_neigh += 1
    if previous[y][x] == 0 and alive_neigh == 3:
        new[y][x] = 1
    elif previous[y][x] == 1 and alive_neigh < 2:
        new[y][x] = 0
    elif previous[y][x] == 1 and alive_neigh > 3:
        new[y][x] = 0



def main():
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 1) \
        == [[1, 0, 1],
            [1, 0, 0],
            [1, 0, 1]]

    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 2) \
        == [[0, 1, 0],
            [1, 0, 0],
            [0, 1, 0]]

    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 3) \
        == [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]]

    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 4) \
        == [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 5) \
        == [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 0) \
        == [[0, 1, 1],
            [1, 1, 1],
            [0, 1, 1]]

    assert life([[1, 1],
                 [1, 1]], 3) \
        == [[1, 1],
            [1, 1]]

    assert life([[1, 1],
                 [0, 1]], 1) \
        == [[1, 1],
            [1, 1]]

    assert life([[1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [1, 0, 0, 1],
                 [0, 0, 1, 1]], 5) \
        == [[0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 0]]


if __name__ == "__main__":
    main()
