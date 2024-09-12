import modulo_agenda
agenda = []

while True:
    print(f"\nAgenda Python")
    print(f"1 - Adicionar um contato")
    print(f"2 - Visualizar a lista de contatos cadastrados")
    print(f"3 - Editar contato")
    print(f"4 - Marcar um contato como favorito")
    print(f"5 - Desmarcar um contato como favorito")
    print(f"6 - Ver lista de contatos favoritos")
    print(f"7 - Apagar qualquer contato")
    print(f"8 - Sair") 
    opcao = int(input(f"\nQual opção deseja? "))
   
    if opcao == 1:
        modulo_agenda.adicionar_contato(agenda)
    elif opcao == 8:
        break
    elif opcao == 2:
        modulo_agenda.visualizar_contato(agenda) 
    elif opcao == 3:
        modulo_agenda.editar_contato(agenda)
    elif opcao == 4:
        modulo_agenda.favoritar_contato(agenda)
    elif opcao == 5:
        modulo_agenda.desfavoritar_contato(agenda)
    elif opcao == 6:
        modulo_agenda.Lista_Favoritos(agenda)
    elif opcao == 7:
        modulo_agenda.deleta_contato(agenda)
