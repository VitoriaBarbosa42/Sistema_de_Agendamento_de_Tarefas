# Dicionários: Armazene as tarefas em um dicionário onde a chave pode ser um ID incremental e o valor é outro dicionário com 
#     nome_tarefa e status (ex: "pendente", "concluída").

#chave - ID incremental : Valor -valor é outro dicionário

from Tarefas import menu_principal
from Tarefas import criar
from Tarefas import ler
from Tarefas import atualizar
from Tarefas import excluir
from Tarefas import solicitat_id

while True:
    inicio = menu_principal()

    if inicio == '1':
        lista_tarefas = criar()

    if inicio == '2':
        try:
            ler(lista_tarefas)
        except NameError:
            print ('Não há tarefas. Adicionear primeiro para vizualiza-las')
        
    if inicio == '3':
        try:
            id = solicitat_id(lista_tarefas)
            if id:
                atualizar(lista_tarefas, id)
            else:
                print('Voltando ao menu principal')
        except NameError:
            print ('Não há tarefas. Adicionear primeiro para atualiza-las')

    if inicio == '4':
        try:
            for chave, valor in lista_tarefas.items():
                print (chave, valor)
            id = solicitat_id(lista_tarefas)
            if id:
                excluir(lista_tarefas, id)
                for chave, valor in lista_tarefas.items():
                    print (chave, valor)
            else:
                print('Voltando ao menu principal')
        except NameError:
            print ('Não há tarefas. Adicionear primeiro para excluir')

    elif inicio == '5':
        print('ATÉ A PROXIMA! :)')
        break