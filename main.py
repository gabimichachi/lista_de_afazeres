while True:
    print('''
        ╔════════════════════════════════════════════════════════╗
        ║                TO-DO LIST - MENU PRINCIPAL             ║
        ╠════════════════════════════════════════════════════════╣
        ║  1. adicionar tarefa                                   ║
        ║  2. listar tarefa                                      ║
        ║  3. concluir                                           ║
        ║  4. excluir tarefa                                     ║
        ║  5. sair                                               ║
        ║                                                        ║
        ╠════════════════════════════════════════════════════════╣
            ''')

    lista_tarefas = []

    # tarefa = input("qual tarefa você quer realizar?")

    #perguntando aqui
    tarefa = int(input("informe o número da tarefa que você deseja realizar: "))

    if tarefa == 1:
        tarefa_add = input("qual tarefa vc deseja adicionar?: ")
        lista_tarefas.append(tarefa_add)

    elif tarefa == 2:
        cont = 0 
        for tarefa in lista_tarefas:
            print(f"{cont} -{tarefa}")
            cont +=1

    elif tarefa == 3:
        concluida = int(input("qual número da lista você concluiu?"))
        lista_tarefas [concluida] = lista_tarefas [concluida] + "✔"

    elif tarefa == 4:
        excluir = int(input("qual item você deseja excluir?: "))
        lista_tarefas.pop(excluir)

    elif tarefa>4:
        print("você saiu")
        break