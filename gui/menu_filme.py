from logica import filme

from logica import historico
from gui import menu_historico

def imprimir_filme(filme):
    print("Titulo: ", filme[0])
    print("Genero: ", filme[1])
    print("Ano: ", filme[2])
    print()

def menu_adicionar():
    print("Adicionar Filme")
    titulo = str(input("Titulo: "))
    genero = str (input("Genero: "))
    ano = int(input("Ano: "))
    filme.adicionar_filme(titulo, genero, ano)

def menu_listar():
    print("Listar Filmes ")
    filmes = filme.listar_filmes()
    for m in filmes:
        imprimir_filme(m)

def menu_buscar():
    print ("Buscar por Titulo ")
    titulo = str(input("Titulo: "))
    m = filme.buscar_filme(titulo)
    if m == None :
        print("Filme nao encontrado")
    else:
        imprimir_filme(m)

def menu_buscar_genero():
    print ("Buscar por Genero ")
    genero = str(input("Genero: "))
    m = filme.buscar_filme_genero(genero)
    if m == None :
        print("Genero nao encontrado")
    else:
        imprimir_filme(m)

def menu_remover():
    print("Remover filme")
    titulo = str(input("Titulo: "))
    m = filme.remover_filme(titulo)
    if m == False:
        print("filme nao encontrado")
    else:
        print("Filme removido")

def inicializar_dados():
    historico.iniciar_historicos()        

def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Filme \n" +
             "(2) Listar Filme \n" +
             "(3) Buscar Filme por Titulo \n" +
             "(4) Remover Filme \n" +
             "(5) Buscar Filme por Genero \n" +
             "(6) Para ver o Historico \n" +
             "(0) Voltar\n"+
            "----------------")

    while(run_filme):
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
            menu_buscar_genero()
        elif (op == 6):
            menu_historico.mostrar_menu()
        elif (op == 0):
            run_filme = False
    


if __name__ == "__main__":
    mostrar_menu()
    
