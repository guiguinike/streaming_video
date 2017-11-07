from logica import ajuda


def imprimir_ajuda(ajuda):
    print("Seu nome: ", ajuda[0])
    print("Telefone: ", ajuda[1])
    print("E-mail: ", ajuda[2])
    print("CPF: ",ajuda[3])
    print("Motivo: ", ajuda[4])
    print("Entraremos em contato em breve")
    print()

    
def menu_adicionar():
    print("Como podemos ajudar? ")
    nome = str(input("Nome : "))
    tel = int(input("Telefone: "))
    email = str(input("E-mail: "))
    cpf = int(input("CPF: "))
    motivo = int(input(" 1 para problemas de pagamento "+"\n 2 para reclamar "+"\n 3 para duvidas "))
    ajuda.adicionar_ajuda(nome, tel, email,cpf, motivo)



def menu_listar():
    print("Ajudas/Reclamações")
    ajudas = ajuda.listar_ajudas()
    for m in ajudas:
        imprimir_ajuda(m)

def menu_remover():
    print("Remover Ajuda/Reclamação")
    cpf = int(input("CPF: "))
    m = ajuda.remover_ajuda(cpf)
    if m == False:
        print("CPF nao encontrado")
    else:
        print("Ajuda/Reclamação removida")

def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar nova Reclamação ou ajuda \n" +
             "(2) Listar Reclamação ou ajuda \n" +
             "(3) Remover Reclamação ou ajuda \n" )

    while(run_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))
        print("")

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_remover()
        elif (op == 0):
            run_filme = False
    


if __name__ == "__main__":
    mostrar_menu()
