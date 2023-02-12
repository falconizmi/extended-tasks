# Napište funkci ‹delete_to_maximal›, která pro dané číslo ‹number›
# najde největší možné číslo, které lze získat smazáním jedné
# desítkové cifry.

def delete_to_maximal(number):
    digits = count_digits(number)
    if digits == 1:
        return number

    while digits > 1:
        num1 = (number // (10 ** (digits - 1))) % 10
        num2 = (number // (10 ** (digits - 2))) % 10
        if num1 < num2:
            return (number // (10 ** digits)) * (10 ** (digits-1)) + number % (10 ** (digits - 1))
        digits -= 1

    return number // 10

# Napište funkci ‹delete_k_to_maximal›, která pro dané číslo
# ‹number› najde největší možné číslo, které lze získat smazáním
# (vynecháním) ‹k› desítkových cifer.


def delete_k_to_maximal(number, k):
    digits = count_digits(number)
    cur_digit = digits

    while cur_digit > 1 and k != 0:
        num1 = (number // (10 ** (cur_digit - 1))) % 10
        num2 = (number // (10 ** (cur_digit - 2))) % 10
        if num1 < num2 and (cur_digit < digits or num1 != 0):
            number = (number // (10 ** cur_digit)) * (10 ** (cur_digit - 1)) + number % (10 ** (cur_digit - 1))
            k -= 1
            digits -= 1
        else:
            cur_digit -= 1

    for _ in range(k):
        number //= 10
    return number


def count_digits(number):
    if number == 0:
        return 1

    digits = 0
    while number != 0:
        number //= 10
        digits += 1
    return digits


def main():
    assert delete_to_maximal(54) == 5
    assert delete_to_maximal(45) == 5
    assert delete_to_maximal(100) == 10
    assert delete_to_maximal(123) == 23
    assert delete_to_maximal(4312) == 432
    assert delete_to_maximal(1231) == 231
    assert delete_to_maximal(2331) == 331

    assert delete_k_to_maximal(2331, 2) == 33
    assert delete_k_to_maximal(22331, 2) == 331
    assert delete_k_to_maximal(12345, 4) == 5
    assert delete_k_to_maximal(1234554321, 8) == 55
    assert delete_k_to_maximal(123123123123, 4) == 33123123
    assert delete_k_to_maximal(123321123321, 4) == 33223321
    assert delete_k_to_maximal(11181118111, 9) == 88


if __name__ == "__main__":
    main()
