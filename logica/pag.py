pags = []

def adicionar_pag(nome, numero, ano,plano):
    pag = [nome, numero, ano, plano]
    pags.append(pag)

def listar_pags():
    return pags

def buscar_pag(nome):
    for m in pags:
        if (m[0] == nome):
            return m
    return False

def remover_pag(nome):
    for m in pags:
        if (m[0] == nome):
            pags.remove(m)
            return True
    return False

def iniciar_pags():
    adicionar_pag("Henrique",123456789,2109,"Basico")
    adicionar_pag("Lucas",966423220,2017,"Padrao")
    adicionar_pag("Guilherme",123964542,2109,"Premium")
