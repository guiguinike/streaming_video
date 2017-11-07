from logica import pag

def imprimir_pag(pag):
    print("Nome do Titular do cartão: ",pag[0])
    print("Numeros do cartão :",pag[1])
    print("Ano de validade: ",pag[2])
    print("Plano escolhido: ", pag[3])
    print()

def menu_adicionar():
    print("Adicionar Cartão")
    nome = str(input("Titular do cartão: "))
    numero = int(input("Numeros do cartão: "))
    ano = int(input("Ano de Validade: "))
    plano = str(input("Escolha o plano Basico, plano Padrao ou plano Premium"))
    pag.adicionar_pag(nome, numero, ano, plano)

def menu_listar():
    print("Listar Cartões")
    pags = pag.listar_pags()
    for m in pags:
        imprimir_pag(m)

def menu_buscar():
    print("Buscar cartao por nome")
    nome = str(input("Nome do Titular: "))
    m = pag.buscar_pag(nome)
    if m == None:
        print("Cartão nao encontrado")
    else:
        imprimir_pag(m)

def menu_remover():
    print("Remover cartao")
    nome = str(input("Nome do titular: "))
    m = pag.remover_pag(nome)
    if m == False:
        print("Cartão nao encontrado")
    else:
        print("Cartão removido")

def mostrar_menu():
    run_pag = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Cartão \n" +
             "(2) Listar Cartões \n" +
             "(3) Buscar Cartão por nome \n" +
             "(4) Remover Cartão \n" +
             "(0) Voltar\n"+
            "----------------")


    while(run_pag):
        print(menu)
        op = int(input("Digite a opção"))

        if(op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):
            menu_buscar()
        elif(op == 4):
            menu_remover()
        elif(op == 0):
            run_pag = False

if __name__ == "__main__":
    mostrar_menu()
