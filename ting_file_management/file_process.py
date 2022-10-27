import sys
from .file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        dic = instance.search(index)
        if dic["nome_do_arquivo"] == path_file:
            return None
    lines = txt_importer(path_file)
    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(obj)
    print(obj)
    return


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return
    else:
        remove = instance.dequeue()
        path_remove = remove["nome_do_arquivo"]
        print(f"Arquivo {path_remove} removido com sucesso")
        return


def file_metadata(instance, position):
    try:
        find = instance.search(position)
        print(find)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return
