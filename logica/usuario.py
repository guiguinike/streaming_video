usuarios = []

def adicionar_usuario(cpf, nome, email, senha):
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for p in usuarios:
        if (p[0] == cpf):
            return p
    return None

def remover_usuario(cpf):
    for p in usuarios:
        if (p[0] == cpf):
            usuarios.remove(p)
            return True
    return False

def iniciar_usuarios():
    adicionar_usuario(0, "Charles Xavier","Charles@gmail.com","mackenzie")
    adicionar_usuario(1, "Gordofredo","lokonha@gmail.com","analise")
    adicionar_usuario(2, "Adilson","Ribeiro@gmail.com","presbiteriana")
    adicionar_usuario(3, "Ronaldo","Brilhamuito@gmail.com","sistema")
    adicionar_usuario(4, "Pai de Familia","Ai_que_delicia@gmail.com","computador")

