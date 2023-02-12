# † Polynomy jste již potkali v příkladu ‹r4_poly› z páté kapitoly.
# Připomeňme si, že polynom je výraz tvaru:
#
#  ⟦  P(x) = aₙxⁿ + … + a₂x² + a₁x + a₀ = ∑₀ⁿ aᵢxⁱ ⟧
#
# Tentokrát budeme polynomy sčítat, odečítat a násobit. Polynom si
# pro účely tohoto příkladu zavedeme jako datovou strukturu
# s operacemi popsanými níže. Polynomy se sčítají a násobí dle
# běžných pravidel – součet ⟦axᵏ + bxᵏ⟧ se do výsledného polynomu
# promítne jako ⟦(a + b)xᵏ⟧, zatímco výraz ⟦axᵏ ⋅ bxˡ⟧ povede na
# člen ⟦abxᵏ⁺ˡ⟧. Nezapomeňte, že při násobení dvou polynomů lze
# stejnou mocninu ⟦x⟧ dostat různými způsoby, třeba ⟦x⋅x³⟧ je totéž
# jako ⟦x²⋅x²⟧. Potřebné algoritmy pro výpočet koeficientů
# výsledného polynomu si jistě již zvládnete z uvedeného odvodit.


from typing import List


class Polynomial:

    # Vytvoří nový polynom. Koeficienty ve vstupním seznamu jsou
    # uloženy v pořadí ⟦aₙ, aₙ₋₁, …, a₁, a₀⟧ a tento seznam smí
    # obsahovat vedoucí nuly. Vnitřní reprezentaci si ovšem můžete
    # zvolit libovolnou.

    def __init__(self, coefs: List[int]) -> None:
        self.coefs: List[int] = []
        first_zero = True
        for i, c in enumerate(coefs):
            if c != 0 or not first_zero or i + 1 == len(coefs):
                first_zero = False
                self.coefs.append(c)
    # Vrátí koeficienty polynomu jako seznam, opět v pořadí ⟦aₙ,
    # aₙ₋₁, …, a₁, a₀⟧. Výsledný seznam nesmí obsahovat vedoucí nuly
    # (tzn. pro nenulový polynom platí ⟦aₙ ≠ 0⟧).

    def get_coefs(self) -> List[int]:
        return self.coefs

    # Čistá funkce, které výsledkem je součet vstupních polynomů
    # ‹self + other›.

    def add(self, other: 'Polynomial') -> 'Polynomial':
        if len(self.get_coefs()) > len(other.get_coefs()):
            longer, shorter = self.get_coefs()[:], other.get_coefs()
        else:
            longer, shorter = other.get_coefs()[:], self.get_coefs()
        for i in range(len(shorter)):
            longer[-1-i] += shorter[-1-i]

        return Polynomial(longer)

    # Čistá funkce, které výsledkem je rozdíl vstupních polynomů
    # ‹self - other›.

    def subtract(self, other: 'Polynomial') -> 'Polynomial':
        if len(self.get_coefs()) > len(other.get_coefs()):
            longer, shorter = self.get_coefs()[:], [-c for c in other.get_coefs()]
        else:
            longer, shorter = [-c for c in other.get_coefs()], self.get_coefs()
        for i in range(len(shorter)):
            longer[-1 - i] += shorter[-1 - i]

        return Polynomial(longer)

    # Čistá funkce, které výsledkem je součin vstupních polynomů
    # ‹self * other›.

    def multiply(self, other: 'Polynomial') -> 'Polynomial':
        coefs = self.get_coefs()
        other_coefs = other.get_coefs()
        count_coef = len(coefs) + len(other_coefs) - 1
        result = [0 for _ in range(count_coef)]
        for i in range(len(coefs)):
            for j in range(len(other_coefs)):
                result[i+j] += coefs[i]*other_coefs[j]

        return Polynomial(result)


def main() -> None:
    p5 = Polynomial([5])
    p10 = Polynomial([1, 0])
    p432 = Polynomial([4, 3, 2])
    p2121 = Polynomial([2, 1, 2, 1])
    p0 = Polynomial([0])

    p005 = Polynomial([0, 0, 5])
    p0432 = Polynomial([0, 4, 3, 2])
    p0000 = Polynomial([0, 0, 0, 0])

    assert p5.get_coefs() == [5]
    assert p10.get_coefs() == [1, 0]
    assert p432.get_coefs() == [4, 3, 2]
    assert p2121.get_coefs() == [2, 1, 2, 1]
    assert p0.get_coefs() == [0]
    assert p005.get_coefs() == [5]
    assert p0432.get_coefs() == [4, 3, 2]
    assert p0000.get_coefs() == [0]

    assert p10.add(p432).get_coefs() == [4, 4, 2]
    assert p2121.add(p432).get_coefs() == [2, 5, 5, 3]
    assert p2121.add(p432).add(p432).get_coefs() == [2, 9, 8, 5]
    assert p2121.add(p432).add(p432).add(p2121).get_coefs() \
        == [4, 10, 10, 6]
    assert p0432.add(p005).get_coefs() == [4, 3, 7]
    assert p0000.add(p0000).get_coefs() == [0]

    assert p2121.subtract(p432).subtract(p432).get_coefs() \
        == [2, -7, -4, -3]
    assert p10.subtract(p432).get_coefs() == [-4, -2, -2]
    assert p432.subtract(p10).get_coefs() == [4, 2, 2]
    assert p0000.subtract(p0000).get_coefs() == [0]
    assert p5.subtract(p5).get_coefs() == [0]

    assert p10.multiply(p10).get_coefs() == [1, 0, 0]
    assert p5.multiply(p5).get_coefs() == [25]
    assert p10.multiply(p432).get_coefs() == [4, 3, 2, 0]
    assert p2121.multiply(p432).get_coefs() == [8, 10, 15, 12, 7, 2]
    assert p005.multiply(p0432).get_coefs() == [20, 15, 10]
    assert p0000.multiply(p0432).get_coefs() == [0]


if __name__ == '__main__':
    main()
