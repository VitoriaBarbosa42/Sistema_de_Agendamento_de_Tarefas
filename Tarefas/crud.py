# crud.py: Funções para Criar, Ler, Atualizar e Excluir tarefas.

def criar():
    id = 0
    dicionario = {}
    while True:
        id += 1 
        while True:
            tarefa = input('Digite a tarefa que gostaria de adicionar: ')
            if len(tarefa) == 0:
                print('Digite algo para continuar ')
            else:
                print(f'Tarefa armezenada: {tarefa} ')
                break
        status = 'pendente'
        dicionario.update({id : {'tarefa': tarefa, 'status': status}})
        while True:
            sair = input('Gostaria de adicionar mais tarefas? Digite [1] para sim e [2] para não')
            if len(sair) == 0:
                print('Digite algo para continuar: ')
            if sair == '2':
                return dicionario
            else:
                break


def ler(dicionario):
    for chave, valor in dicionario.items():
        print(chave, valor)



def atualizar(dicionario, id):
    try:
        while True:
            print('Digite o numero que repesenta o que gostaria de atualizar: ')
            atualizacao = input('Digite [1] para a tarefa e [2] para o Status [3] para sair')

            if atualizacao == '1':
                while True:
                    nova_tarefa = input('Digite sua nova tarefa: ')
                    if len(nova_tarefa) == 0:
                        print('Digite algo para continuar')
                    else:
                        dicionario [id]['tarefa'] = nova_tarefa
                        print (f'Tarefa {nova_tarefa} atualizada com Sucesso')
                        break

            elif atualizacao == '2':
                while True:
                    print('Qual status da sua atividade: ')
                    status_atualizado = input('[1]Pendente [2]Concluida')

                    if status_atualizado == '1':
                        dicionario [id]['status'] = 'Pendente'
                        print (f'Status: {status_atualizado}')
                        break
                    elif status_atualizado == '2':
                        dicionario [id]['status'] = 'Concluído'
                        print (f'Status: {status_atualizado}! PARABÊNS PELA CONCLUSÃO :)')
                        break

            elif atualizacao == '3':
                print('Voltando ao Menu principal')
            elif len(atualizacao) == 0:
                print('Digite algo para continuar')
            else:
                print('digite um valor valido')

                return dicionario
    except KeyError:
        print ('ID invalido')

        


def excluir(dicionario, id):
    try:    
        dicionario.pop(id)
        return dicionario
    except KeyError:
        print ('ID invalido')




