lista_tarefa = []

#--- Criar as tarefas (por: thiago)---
while True:
    nova_tarefa = input("Digite uma tarefa (ou 'sair'): ")

    if nova_tarefa.lower()== "sair":
        break
    
    lista_tarefa.append(nova_tarefa)


for i, t in enumerate(lista_tarefa, start=1):
    print(f"{i}, {t}")

# --- gerenciador de tarefa (por: thiago)---
while True:
    print("\n--- SUAS TAREFAS ---")
    if len(lista_tarefa) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, t in enumerate(lista_tarefa, start=1):
            print(f"{i}. {t}")

    print("\nO que deseja fazer?")
    print("1 - Apagar uma tarefa")
    print("2 - Substituir uma tarefa")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite o número da tarefa que deseja apagar: "))
        if 1 <= numero <= len(lista_tarefa):
            removida = lista_tarefa.pop(numero - 1)
            print(f"Tarefa '{removida}' removida com sucesso!")
        else:
            print("Número inválido.")

    elif opcao == "2":
        numero = int(input("Digite o número da tarefa que deseja substituir: "))
        if 1 <= numero <= len(lista_tarefa):
            nova = input("Digite a nova tarefa: ")
            lista_tarefa[numero - 1] = nova
            print("Tarefa substituída com sucesso!")
        else:
            print("Número inválido.")

    elif opcao == "3":
        print("Tchauzinho!")
        break

    else:
        print("Opção inválida, tente novamente.")








