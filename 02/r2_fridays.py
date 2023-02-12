# Napište funkci, která spočítá počet pátků 13. v daném roce ‹year›.
# Parametr ‹day_of_week› udává den v týdnu, na který v daném roce
# padne 1. leden. Dny v týdnu mají hodnoty 0–6, počínaje pondělím
# s hodnotou 0.

def fridays(year, day_of_week):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 400 == 0) and (year % 100 == 0):
        months[1] = 29
    elif (year % 4 == 0) and (year % 100 != 0):
        months[1] = 29

    total = 0
    cur_day = 4 - day_of_week
    cur_month = 1
    while cur_month <= 12:
        if cur_day == 12:
            total += 1

        cur_day += 7
        if cur_day >= months[cur_month-1]:
            cur_day = cur_day % months[cur_month-1]
            cur_month += 1

    return total

def main():
    assert fridays(2020, 2) == 2
    assert fridays(2019, 1) == 2
    assert fridays(2018, 0) == 2
    assert fridays(2017, 6) == 2
    assert fridays(2016, 4) == 1
    assert fridays(2015, 3) == 3
    assert fridays(2012, 6) == 3
    assert fridays(2000, 5) == 1
    assert fridays(1996, 0) == 2
    assert fridays(1643, 3) == 3
    assert fridays(1501, 1) == 2


if __name__ == "__main__":
    main()
