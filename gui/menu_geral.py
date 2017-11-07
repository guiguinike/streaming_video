from logica import usuario
from gui import menu_usuario

from logica import filme
from gui import menu_filme

from logica import ajuda
from gui import menu_ajuda




def inicializar_dados():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()
    ajuda.iniciar_ajudas()
    


def mostrar_menu():
    run_menu = True

    inicializar_dados()


    menu = ("\n----------------\n"+
             "(1) Menu Usuario \n" +
             "(2) Menu Filme \n" +
             "(3) Menu Ajuda \n" +
             "(0) Sair\n"+
            "----------------")

    while(run_menu):
        print(menu)

        op = int(input("Digitar a opção: "))

        if op == 1:
            menu_usuario.mostrar_menu()
        elif op == 2:
            menu_filme.mostrar_menu()
        elif op == 3:
            menu_ajuda.mostrar_menu()
        elif op == 0:
            print("Saindo do programa...")
            run_menu = False
        else:
            print("Valor Invalido")
