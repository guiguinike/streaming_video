from logica import usuario

from logica import historico
from gui import menu_historico

from logica import pag
from gui import menu_pag


def imprimir_usuario(usuario):
    print ("CPF: ",  usuario[0])
    print ("Nome: ", usuario[1])
    print ("E-mail: ", usuario[2])
    print ("Senha: ", usuario[3])

def menu_adicionar():
    print("Adicionar Usuario")
    cpf = int(input("CPF: "))
    nome = str (input("Nome: "))
    email = str(input("E-Mail: "))
    senha = str(input("Senha: "))
    usuario.adicionar_usuario(cpf, nome, email, senha)

def menu_listar():
    print("Listar Usuarios")
    usuarios = usuario.listar_usuarios()
    for p in usuarios:
        imprimir_usuario(p)

def menu_buscar():
    print("Buscar usuario por CPF ")
    cpf = int(input("CPF: "))
    p = usuario.buscar_usuario(cpf)
    if p == None:
        print("Usuario nao encontrado")
    else:
        imprimir_usuario(p)

def menu_remover():
    print("Remover Usuario")
    cpf = int(input("CPF: "))
    p = usuario.remover_usuario(cpf)
    if p == False:
        print("Usuario nao encontrado")
    else:
        print("Usuario removido")


def inicializar_dados():
    historico.iniciar_historicos()
    pag.iniciar_pags()

def mostrar_menu():
    run_usuario = True

    inicializar_dados()

    
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Usuario \n" +
             "(2) Listar Usuario \n" +
             "(3) Buscar Usuario por CPF \n" +
             "(4) Remover Usuario \n" +
             "(5) Mostrar Historico \n" +
             "(6) EScolher Plano \n" +
             "(0) Voltar\n"+
            "----------------")
    
    
    while(run_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 5):
            menu_historico.mostrar_menu()
        elif (op == 6):
            menu_pag.mostrar_menu()
        elif (op == 0):
            run_usuario = False
    








