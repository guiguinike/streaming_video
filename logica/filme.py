filmes = []

def adicionar_filme(titulo, genero, ano):
    filme = [titulo, genero, ano]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(titulo):
    for m in filmes:
        if (m[0] == titulo):
            return m
    return False

def buscar_filme_genero(genero):
    for m in filmes:
        if (m[1] == genero):
            return m
    return False

def remover_filme(titulo):
    for m in filmes:
        if m[0] == titulo:
            filmes.remove(m)
            return True
    return False


def iniciar_filmes():
    adicionar_filme("Piratas", "Aventura",2014)
    adicionar_filme("Deus não esta morto", "Drama",2004)
    adicionar_filme("Homem-Aranha", "Ficção",2010)
    adicionar_filme("Carros", "Desenho",2009)
    adicionar_filme("ijuu", "Aventura",2014)
