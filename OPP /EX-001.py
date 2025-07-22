class Pessoa:
    def __init__(self):
        self.nome = "diego"
        self.sexo = "masculino"
        self.cpf = "cpf"
        self.ativo = "ativo"

    
    def mudar_nome(self, nome):
        self.nome = nome


diego = Pessoa()


nome = input('nome: ')

diego.mudar_nome(nome)
print(diego.nome)