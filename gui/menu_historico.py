from logica import historico


def imprimir_historico(historico):
    print("CPF: ",historico[0])
    print("Filme: ",historico[1])

def menu_adicionar():
    print("Registrar Filme")
    cpf = int(input("CPF: "))
    titulo = str(input("Nome do filme: "))
    historico.adicionar_historico(cpf, titulo)

def menu_listar():
    print("Listar filmes assistidos")
    historicos = historico.listar_historicos()
    for p in historicos:
        imprimir_historico(p)

def mostrar_menu():
    run_historico = True
    menu = ("\n----------------\n"+
             "(1) Adicionar filme a lista de assistidos \n" +
             "(2) Listar filmes assistidos \n" +
            " (0) Para Voltar ")
    while(run_historico):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif (op == 0):
            run_historico = False
