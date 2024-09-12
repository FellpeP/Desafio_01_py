agenda = []
import modulo_agenda

while True:
    print(f"\nAgenda Pythom")
    print(f"1 - Adicionar um contato")
    print(f"2 - Visualizar a lista de contatos cadastrados")
    print(f"3 - Editar contato")
    print(f"4 - Marcar um contato como favorito")
    print(f"5 - Desmacar um contato como favorito")
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













#Sobre o desafio
#Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar 
# e marcar um contato como favorito. O resultado da aplicação deve ser 
# apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.

#Regras da aplicação
#A aplicação deve iniciar mostrando uma lista de opções do que é possível
#fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
#Deve ser possível adicionar um contato
#O contato pode ter os dados:
#Nome
#Telefone
#Email
#Favorito (está opção é para poder marcar um contato como favorito)
#Deve ser possível visualizar a lista de contatos cadastrados
#Deve ser possível editar um contato
#Deve ser possível marcar/desmarcar um contato como favorito
#Deve ser possível ver uma lista de contatos favoritos
#Deve ser possível apagar um contato