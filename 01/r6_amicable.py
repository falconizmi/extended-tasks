# † Napište predikát, který určí, jsou-li 2 čísla spřátelená
# (amicable). Spřátelená čísla jsou dvě přirozená čísla taková, že
# součet všech kladných dělitelů jednoho čísla (kromě čísla
# samotného) se rovná druhému číslu, a naopak – součet všech
# dělitelů druhého čísla (kromě něho samotného) se rovná prvnímu.

def get_total_div(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total

def amicable(a, b):
    return get_total_div(a) == b and a == get_total_div(b)


def main():
    assert not amicable(136, 241)
    assert not amicable(1, 1)
    assert amicable(220, 284)
    assert amicable(1184, 1210)
    assert amicable(2620, 2924)
    assert not amicable(1190, 1212)
    assert not amicable(349, 234)


if __name__ == "__main__":
    main()
