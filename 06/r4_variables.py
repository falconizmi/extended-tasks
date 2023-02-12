from typing import Dict, Tuple

# Uvažujme jednoduché aritmetické výrazy se sčítáním a násobením.
# Budeme je ukládat do dvojice slovníků (‹expr› a ‹const›), a to
# následovně:
#
#  • klíč je vždy jméno proměnné (řetězec)
#  • hodnota ve slovníku ‹expr› je trojice:
#    ◦ první složka je operátor ‹'*'› nebo ‹'+'›
#    ◦ druhá a třetí složka jsou operandy – názvy proměnných
#  • hodnota ve slovníku ‹const› je číslo
#
# Každá proměnná se objeví v nejvýše jednom slovníku. Proměnné,
# které se nenachází v žádném z nich jsou rovny nule.

# Napište čistou funkci, která dostane jako parametry slovníky
# ‹expr› a ‹const› a název proměnné. Výsledkem bude hodnota této
# proměnné.


def evaluate(expr: Dict[str, Tuple[str, str, str]],
             const: Dict[str, int], var: str) -> int:

    if var in const:
        return const[var]
    elif var not in expr:
        return 0
    op, var1, var2 = expr[var]
    if op == "+":
        return evaluate(expr, const, var1) + evaluate(expr, const, var2)
    return evaluate(expr, const, var1) * evaluate(expr, const, var2)


def main() -> None:
    assert evaluate({}, {'a': 1}, 'a') == 1
    assert evaluate({'x': ('+', 'a', 'a')}, {'a': 1}, 'x') == 2
    assert evaluate({'x': ('+', 'a', 'b')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'y') == 9


if __name__ == "__main__":
    main()
