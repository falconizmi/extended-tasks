# † Nechť ⟦A⟧ je Fibonacciho posloupnost s členy ⟦aₙ⟧ a ⟦B⟧ je
# posloupnost taková, že má na ⟦i⟧-té pozici ⟦aᵢ⟧-tý prvek
# posloupnosti ⟦A⟧, tj. prvek s indexem ⟦aᵢ⟧ (nikoliv prvek
# s indexem ⟦i⟧). Napište funkci, která sečte prvních ‹count› prvků
# posloupnosti ⟦B⟧ (t.j. ty prvky posloupnosti ⟦A⟧, kterých «indexy»
# jsou po sobě jdoucí Fibonacciho čísla).

# Například ‹fibfibsum(6)› se vypočte takto:
# ⟦ a₁ + a₁ + a₂ + a₃ + a₅ + a₈ = 1 + 1 + 1 + 2 + 5 + 21 = 31 ⟧

def fibfibsum(count):
    total = 2
    current_index = 2
    f1_index = 1
    f2_index = 2
    f1_value = 1
    f2_value = 1
    count -= 2

    while count != 0:
        if current_index == f2_index:
            total += f2_value
            f1_index, f2_index = f2_index, f1_index + f2_index
            count -= 1
        f1_value, f2_value = f2_value, f1_value + f2_value
        current_index += 1
    return total


def main():
    assert fibfibsum(3) == 3
    assert fibfibsum(5) == 10
    assert fibfibsum(6) == 31
    assert fibfibsum(7) == 264
    assert fibfibsum(10) == 139589576542


if __name__ == "__main__":
    main()
