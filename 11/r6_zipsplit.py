from zipfile import ZipFile
from typing import List, Dict
import os
import glob


# Procedura ‹split_zip_by_size› má dva parametry: název vstupního
# ZIP souboru a maximální velikost. Procedura pro vstupní soubor
# ‹input.zip› vytvoří soubory ‹input.NN.zip›, kde ‹NN› je v rozsahu
# ‹01› až ‹99›, a kde každý:
#
#  • je nejvýše zadané «nekomprimované» velikosti, nebo
#  • obsahuje pouze jediný soubor.
#
# Metadata do velikosti nepočítejte. Případy, kdy by vzniklo více
# než 99 dílčích souborů, neuvažujte.


def split_zip_by_size(zip_name: str, max_size: int) -> None:
    with ZipFile(zip_name, "r") as z_file:
        files = z_file.infolist()
        cur_size = 0
        cur_zip_file = None
        count_file = 1
        if len(files) != 0:
            cur_zip_file = ZipFile(f"{zip_name[:-4]}.{count_file:02}.zip", 'w')

        for file in files:
            if file.file_size == 0:
                continue

            if cur_size + file.file_size > max_size:
                assert cur_zip_file is not None
                cur_zip_file.close()
                count_file += 1
                cur_zip_file = ZipFile(f"{zip_name[:-4]}.{count_file:02}.zip", 'w')
                cur_size = 0
            cur_size += file.file_size
            assert cur_zip_file is not None
            with z_file.open(file, "r") as f:
                cur_zip_file.writestr(file.filename, f.read())

        if cur_zip_file is not None:
            cur_zip_file.close()



def main() -> None:
    import shutil
    shutil.copy("zz.zipsplit.zip", "zt.zipsplit.zip")
    split_zip_test("zt.zipsplit.zip", 1000)
    split_zip_test("zt.zipsplit.zip", 500)
    split_zip_test("zt.zipsplit.zip", 50)
    split_zip_test("zt.zipsplit.zip", 5)
    split_zip_test("zt.zipsplit.zip", 1000000000)


def split_zip_test(orig_zip: str, max_size: int) -> None:
    for filename in glob.glob("./" + orig_zip[:-3] + "??.zip"):
        os.remove(filename)

    files_counts: Dict[str, int] = {}
    orig_files_contents: Dict[str, str] = {}

    with ZipFile(orig_zip, "r") as zip_file:
        for curr in zip_file.infolist():
            if curr.file_size > 0:
                files_counts[curr.filename] = 0
                orig_files_contents[curr.filename] = \
                    zip_file.read(curr.filename).decode('UTF-8')

    split_zip_by_size(orig_zip, max_size)

    found_zip_names: List[str] = []

    for filename in glob.glob("./" + orig_zip[:-3] + "??.zip"):
        with ZipFile(filename, "r") as zip_file:
            curr_zip_size = 0
            found_zip_names.append(filename)

            for curr in zip_file.infolist():
                curr_zip_size += curr.file_size

                assert curr.filename in files_counts, (
                    "redundant file", curr.filename, filename)
                assert files_counts[curr.filename] == 0, (
                    "duplicate file", curr.filename, filename)
                files_counts[curr.filename] += 1

                assert orig_files_contents[curr.filename] == \
                       zip_file.open(curr.filename).read().decode(
                           'UTF-8'), ("wrong file content",
                                      curr.filename)

            assert (len(zip_file.namelist()) == 1 or
                    curr_zip_size <= max_size), (
                        "zip too big", filename)

    for name, count in files_counts.items():
        assert count == 1, ("missing file", name)

    found_zip_names.sort()
    for i in range(len(found_zip_names)):
        assert int(found_zip_names[i][-6:][:-4]) == i + 1, (
            i + 1, "wrong zipfile num")


if __name__ == "__main__":
    main()
