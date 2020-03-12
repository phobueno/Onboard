class Usuario(object):
    def __init__(self, nome, idd, email, cpf, dataCriacao, status, perfil):
        self.nome = nome
        self.id = idd
        a = self.validacaoEmail(email)
        if(a):
            self.email = email
        b = self.validacaoCpf(cpf)
        if(b):
            cpf = cpf[:3]+"."+cpf[3:]
            cpf = cpf[:8]+"."+cpf[8:]
            cpf = cpf[:12]+"-"+cpf[12:]
            self.cpf = cpf
        self.dataCriacao = dataCriacao
        self.status = status
        self.perfil = perfil

    def validacaoEmail(self, a):
        c = a.find('@')
        b = a.find('.')
        assert (c > b)
        return True

    def validacaoCpf(self, a):
        assert (a == 11)
        return True


class Teleconsultoria:
    pass
