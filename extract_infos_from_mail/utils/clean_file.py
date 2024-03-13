def clean_file(file_path) -> str:
    with open(file_path, "r") as file:
        content = file.read()

    content = content.replace("\n\n", "\n")

    content = content.replace("--------------", "")
    content = content.replace("---------", "")
    content = content.replace("--------", "")
    content = content.replace("------", "")

    content = "\n".join(
        [line for line in content.split("\n") if not line.startswith("De:")]
    )
    content = "\n".join(
        [line for line in content.split("\n") if not line.startswith("Envoyé:")]
    )
    content = "\n".join(
        [line for line in content.split("\n") if not line.startswith("À:")]
    )
    content = "\n".join(
        [line for line in content.split("\n") if not line.startswith("Objet:")]
    )

    content = content.replace("Code pro partenaire :", "BEGIN\nCode pro partenaire :")

    clean_file_path = file_path.replace(".txt", "_clean.txt")

    with open(clean_file_path, "w") as file:
        file.write(content)

    return clean_file_path
