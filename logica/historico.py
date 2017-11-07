historicos = []

def adicionar_historico(cpf, titulo):
    historico = [cpf, titulo]
    historicos.append(historico)

def listar_historicos():
    return historicos


def iniciar_historicos():
    adicionar_historico(0, "Piratas")
    
