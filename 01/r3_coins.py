# Uvažme, že chceme přesně zaplatit sumu ‹value› českými mincemi
# (denominace 1, 2, 5, 10, 20 a 50 korun). Spočtěte, kolik nejméně
# mincí potřebujeme.

def coins(value):
    total = 0
    type_coin = [50, 20, 10, 5, 2, 1]

    for c in type_coin:
        total += value // c
        value = value % c
        if value == 0:
            break

    return total



def main():
    assert coins(10) == 1
    assert coins(23) == 3
    assert coins(48) == 5
    assert coins(92) == 4
    assert coins(314) == 9
    assert coins(1043) == 24


if __name__ == "__main__":
    main()
