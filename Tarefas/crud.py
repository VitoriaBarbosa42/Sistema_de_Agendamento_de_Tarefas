# crud.py: Funções para Criar, Ler, Atualizar e Excluir tarefas.

def criar(id, dicionario):
    while True:
        id += 1 
        while True:
            tarefa = input('Digite a tarefa que gostaria de adicionar: ')
            print()
            if len(tarefa) == 0:
                print('Digite algo para continuar ')
                print()
            else:
                print(f'Tarefa armazenada: {tarefa} ')
                print()
                status = 'pendente'
                dicionario.update({id : {'tarefa': tarefa, 'status': status}})
                break
        while True:
            sair = input('Gostaria de adicionar mais tarefas? Digite [1] para sim e [2] para não ')
            print()
            if len(sair) == 0:
                print('Digite algo para continuar: ')
                print()
            elif sair == '1':
                print ('Adicione mais uma tarefa: ')
                print()
                break
            elif sair == '2':
                return dicionario
            else:
                print('Valor invalido')
                print()



def ler(dicionario):
    for chave, valor in dicionario.items():
        print (chave, valor)
    print()




def atualizar(dicionario, id):
    
    while True:
        print('Digite o numero que representa o que gostaria de atualizar: ')
        atualizacao = input('Digite [1] para a tarefa e [2] para o Status [3] para sair ')

        if atualizacao == '1':
            while True:
                nova_tarefa = input('Digite sua nova tarefa: ')
                print()
                if len(nova_tarefa) == 0:
                    print('Digite algo para continuar')
                    print()
                else:
                    dicionario [id]['tarefa'] = nova_tarefa
                    print (f'Tarefa {nova_tarefa} atualizada com Sucesso')
                    print()
                    break

        elif atualizacao == '2':
            while True:
                print('Qual status da sua atividade: ')
                status_atualizado = input('[1]Pendente [2]Concluida ')
                print()

                if status_atualizado == '1':
                    dicionario [id]['status'] = 'Pendente'
                    print (f'Status: {status_atualizado}')
                    print()
                    break
                elif status_atualizado == '2':
                    dicionario [id]['status'] = 'Concluído'
                    print (f'Status: {status_atualizado}! PARABÊNS PELA CONCLUSÃO :)')
                    print()
                    break

        elif atualizacao == '3':
            print('Voltando ao Menu principal')
            print()
            break
        elif len(atualizacao) == 0:
            print('Digite algo para continuar')
            print()
        else:
            print('digite um valor valido')
            print()

            return dicionario


        


def excluir(dicionario, id):   
    dicionario.pop(id)
    return dicionario




