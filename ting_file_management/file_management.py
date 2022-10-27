import sys
from os.path import exists


def txt_importer(path_file):
    if exists(path_file) is False:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return
    with open(path_file, mode="r") as file:
        data = list(file)
        listData = []
        for row in data:
            newLine = row.rstrip("\n")
            listData.append(newLine)
    return listData