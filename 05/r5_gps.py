# Napište a otypujte funkci ‹parse_gps›, která přečte GPS souřadnice
# ze vstupního řetězce ‹raw›. Očekávaný vstup je ve formátu
# ‹lat=X;lon=Y› kde ‹X› a ‹Y› jsou čísla s povinnou desetinnou
# tečkou. Je-li vstup ve správném formátu a obě souřadnice spadají
# do svého přípustného rozsahu, funkce vrátí dvojici hodnot typu
# ‹float›, které odpovídají číselným hodnotám zeměpisné šířky
# (latitude) a délky (longitude). V opačném případě vrátí ‹None›.
# Přípustný rozsah zeměpisné šířka je -90 až 90 a zeměpisné délky
# -180 až 180.

from typing import List, Optional, Tuple

def parse_gps(raw: str) -> Optional[Tuple[float,float]]:
    if ";" not in raw:
        return None
    lat_xy = raw.split(";")

    if "lat=" not in lat_xy[0] or "lon=" not in lat_xy[1]:
        return None
    string_x, string_y = lat_xy[0].split("lat=")[1], lat_xy[1].split("lon=")[1]
    if "." not in string_x or "." not in string_y:
        return None
    try:
        x = float(string_x)
        y = float(string_y)
    except:
        return None
    if not(-90 <= x and x <= 90 and
        -180 <= y and y <= 180):
        return None

    return x, y




# Dále napište a otypujte funkci ‹parse_gps_stream›, která přečte
# seznam GPS souřadnic a vrátí seznam dvojic s číselnými hodnotami
# souřadnic. Souřadnice na vstupu jsou každá na vlastním řádku.
# Nekóduje-li kterýkoliv řádek GPS souřadnici, funkce vrátí ‹None›.

def parse_gps_stream(raw: str) -> Optional[List[Tuple[float,float]]]:
    if len(raw) == 0:
        return []

    result = []
    for line in raw.split("\n"):
        coords = parse_gps(line)
        if coords is None:
            return None
        result.append(coords)
    return result


def main() -> None:
    assert parse_gps("lat=49.2099839;lon=16.5989169") \
        == (49.2099839, 16.5989169)
    assert parse_gps("lat=49.2099839;lon=-16.5989169") \
        == (49.2099839, -16.5989169)
    assert parse_gps("lat=-49.2099839;lon=16.5989169") \
        == (-49.2099839, 16.5989169)

    assert parse_gps("lat=99.2099839;lon=16.5989169") is None, \
        "latitude out of range"
    assert parse_gps("lat=-99.2099839;lon=16.5989169") is None, \
        "latitude out of range"
    assert parse_gps("lat=49.2099839;lon=-196.5989169") is None, \
        "longitude out of range"
    assert parse_gps("lat=49.2099839;lon=196.5989169") is None, \
        "longitude out of range"
    assert parse_gps("text") is None, "invalid format"
    assert parse_gps("49.2099839;16.5989169") is None, "invalid format"
    assert parse_gps("lat=49.2099839 lon=16.5989169") is None, "invalid format"
    assert parse_gps("lon=16.5989169;lat=49.2099839") is None, "invalid format"
    assert parse_gps("lat=49;lon=16") is None, "invalid format"
    assert parse_gps("lat=49;2099839;lon=16;5989169") is None, "invalid format"
    assert parse_gps("lat=-49.2O99839;lon=16.5989l69") is None, \
        "invalid format"

    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
lat=50.0835494;lon=14.4341414""") \
        == [(49.2099839, 16.5989169),
            (48.1516986, 17.1093064),
            (50.0835494, 14.4341414)]

    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-17.1093064
lat=-50.0835494;lon=14.4341414""") \
        == [(49.2099839, 16.5989169),
            (48.1516986, -17.1093064),
            (-50.0835494, 14.4341414)]

    assert parse_gps_stream("") == []

    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-189.1093064
lat=-50.0835494;lon=14.4341414""") \
        is None

    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
invalid entry""") \
        is None


if __name__ == "__main__":
    main()
