ajudas = []

def adicionar_ajuda(nome, tel, email, cpf, motivo):
    ajuda = [nome, tel, email, cpf, motivo]
    ajudas.append(ajuda)

def listar_ajudas():
    return ajudas

def remover_ajuda(cpf):
    for m in ajudas:
        if m[3] == cpf:
            ajudas.remove(m)
            return True
    return False

def iniciar_ajudas():
    adicionar_ajuda("henrique",22938218,"henriquemagana@gmail.com",479,2)
    adicionar_ajuda("Lucas",12345678,"boiola@gmail.com",244,3)
