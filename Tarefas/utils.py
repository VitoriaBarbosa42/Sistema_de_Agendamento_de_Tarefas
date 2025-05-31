# Funções utilitárias (ex: uma função para validar entrada do usuário, ou para exibir tarefas formatadas)

def menu_principal():
    print ('MENU PRINCIPAL DO GERENCIADOR DE TAREFAS :)')
    print('_________________________________________')

    while True:
        print('Escolha uma opção abaixo: ')
        inicio = input('[1] Criar novas tarefas [2] Ver tarefas [3] Atualizar tarefa [4] Excluir tarefas [5] Sair: ')
        if len(inicio) == 0:
            print('Digite um valor para continuar')
        elif len(inicio) == 1 and inicio in '12345':
            if inicio == '1':
                inicio = '1'
                print(f'Opção escolhida: Criar novas tarefas')
                return inicio
            elif inicio == '2':
                inicio = '2'
                print(f'Opção escolhida: Ver tarefas')
                return inicio
            elif inicio == '3':
                inicio = '3'
                print(f'Opção escolhida: Atualizar tarefa')
                return inicio
            elif inicio == '4':
                inicio = '4'
                print(f'Opção escolhida: Excluir tarefas')
                return inicio
            elif inicio == '5':
                inicio = '5'
                print(f'Opção escolhida: Sair')
                return inicio            
        else:
            print('Opção invalida. Tente novamente')
            print()

def solicitat_id(dicionario):
    try:    
        id = int(input('Digite o ID que você gostaria de consultar: '))
        print (dicionario[id])
        return id
    except KeyError:
        print ('ID invalido')
    except ValueError:
        print ('ID não identificado')
    except NameError:
        print ('Não tem itens na sua lista')

