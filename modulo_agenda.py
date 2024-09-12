def adicionar_contato(agenda):
    print(f"Dados para cadastro de contato\n")
    nome = input(f"Nome: ")
    telefone = input(f"Telefone: ")
    email = input(f"Email: ")

    agenda.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    })
    print(f"dados cadastro com sucesso\n")
    return


def visualizar_contato(agenda):
    print(f"\ncontatos salvos")
    for cadastrados in agenda:
        print(f"Nome: ", cadastrados["nome"])
        print(f"Telefone: ", cadastrados["telefone"])
        print(f"Email: ", cadastrados["email"])
    return


def editar_contato(agenda):
    nome = input(f"Digite o nome do contado deseja editar!! ")
    for cadastrados in agenda:
        if cadastrados["nome"] == nome:
            print(f"\nContado encontrado")
            print(f"Por favor digite novos dados\n")
            cadastrados["nome"] = input(f"Nome: ")
            cadastrados["telefone"] = input(f"Telefone: ")
            cadastrados["email"] = input(f"Email: ")
        else:
            print("contado não cadastrado")
    return


def favoritar_contato(agenda):
    nome = input("Digite um nome do contato que deseja favoritar: ")
    for cadastrados in agenda:
        if cadastrados["nome"] == nome:
            if cadastrados["favorito"]:
                print("Contato ja esta marcado como favorito")
            else:
                cadastrados["favorito"] = True
                print("Contato salvo como favorito ✅", nome)
    return


def desfavoritar_contato(agenda):
    nome = input("Digite um nome do contato que deseja desfavoritar: ")
    for cadastrados in agenda:
        if cadastrados["nome"] == nome:
            if cadastrados["favorito"]:
                print("Contato ja esta desfavoritado")
                cadastrados["favorito"] = False
    return


def Lista_Favoritos(agenda):
    print("\nLista de contatos favoritos:")
    for cadastrados in agenda:
        if cadastrados["favorito"]:
            print("✅", cadastrados["nome"])
    return


def deleta_contato(agenda):
    nome = input(f"Qual contato deeja deleta? ")
    for i, cadastrados in enumerate(agenda):
        if cadastrados["nome"] == nome:
            agenda.pop(i)
    return
