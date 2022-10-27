def exists_word(word, instance):
    array = []
    for rows in range(len(instance)):
        ocorrencias = []
        lines = instance.search(rows)["linhas_do_arquivo"]
        for index, line in enumerate(lines):
            if word.lower() in line.lower():
                path_file = instance.search(rows)["nome_do_arquivo"]
                count = index + 1
                ocorrencias.append({"linha": count})
        if len(ocorrencias) > 0:
            obj = {
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": ocorrencias
                }
            array.append(obj)
    return array


def search_by_word(word, instance):
    array = []
    for rows in range(len(instance)):
        ocorrencias = []
        lines = instance.search(rows)["linhas_do_arquivo"]
        for index, line in enumerate(lines):
            if word.lower() in line.lower():
                path_file = instance.search(rows)["nome_do_arquivo"]
                count = index + 1
                ocorrencias.append({"linha": count, "conteudo": line})
        if len(ocorrencias) > 0:
            obj = {
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": ocorrencias
                }
            array.append(obj)
    return array
