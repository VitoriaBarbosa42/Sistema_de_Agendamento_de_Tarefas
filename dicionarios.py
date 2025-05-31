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
    lista_tarefas = {}

    if inicio == '1':
        lista_tarefas = criar()

    elif inicio == '2':
        print(ler(lista_tarefas))
        
    elif inicio == '3':
        id = solicitat_id
        atualizar(lista_tarefas, id)


    elif inicio == '4':
        id = solicitat_id
        excluir()

    elif '5':
        print('ATÉ A PROXIMA! :)')
        break