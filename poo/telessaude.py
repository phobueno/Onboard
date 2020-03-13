class Usuario(object):
    def __init__(self, nome, idd, email, cpf, dataCriacao, status, perfil=""):
        self.nome = nome
        self.id = idd
        self.validacaoEmail(email)
        self.email = email
        self.validacaoCpf(len(cpf))
        cpf = cpf[:3]+"."+cpf[3:]
        cpf = cpf[:7]+"."+cpf[7:]
        cpf = cpf[:11]+"-"+cpf[11:]
        self.cpf = cpf
        self.dataCriacao = dataCriacao
        self.status = status
        self.perfil = perfil

    def validacaoEmail(self, a):
        c = a.find('@')
        b = a.find('.')
        assert (c < b and c != (-1))
        return True

    def validacaoCpf(self, a):
        assert (a == 11)
        return True


class Teleconsultoria(object):
    def __init__(self, idt, teleconsultor, solicitante, dadosCaso,
                 datasInicio, dataFim, status):
        self.idt = idt
        self.teleconsultor = teleconsultor
        self.solicitante = solicitante
        self.dadosCaso = dadosCaso
        self.datasInicio = datasInicio


class Unidade(object):
    def __init__(self, idu, cnes, nome, municipio, uf, telefone, tipo, status):
        self.idu = idu
        self.cnes = cnes
        self.nome = nome
        self.municipio = municipio
        self.uf = uf
        self.telefone = telefone
        self.tipo = tipo
        self.status = status


class UsuarioUnidade(object):
    def __init__(self, iduu, idd, idu, perfil):
        self.iduu = iduu
        self.idd = idd
        self.idu = idu
        self.perfil = perfil


def teleconsulta(teleconsultor, solicitante):
    a = Teleconsultoria(1,
                        teleconsultor,
                        solicitante,
                        "neurologia",
                        "11/03/2020 13:30",
                        "11/03/2020 14:10",
                        "encerrado")
    return a


U = Usuario("Paulo",
            1,
            "paulo@fucspa.com",
            "03486894393",
            "13:30",
            True,
            "Teleconsultor")

UU = Usuario("Pedro",
             2,
             "pedri@fucspa.com",
             "76528239387",
             "13:30",
             True,
             "Solicitante")

b = teleconsulta(U, UU)
print(b.idt)
print(b.teleconsultor.cpf)
