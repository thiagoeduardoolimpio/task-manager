lista_tarefa = []
while True:
    nova_tarefa = input("Digite uma tarefa (ou 'sair'): ")

    if nova_tarefa.lower()== "sair":
        break
    
    lista_tarefa.append(nova_tarefa)


for i, t in enumerate(lista_tarefa, start=1):
    print(f"{i}, {t}")









