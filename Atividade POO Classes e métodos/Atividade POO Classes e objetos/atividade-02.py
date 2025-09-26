class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        if len(str(novo_cpf)) == 11:
            self.__cpf = novo_cpf
        else:
            print("CPF inválido! Deve ter 11 dígitos.")

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        if len(str(nova_identidade)) >= 5:
            self.__identidade = nova_identidade
        else:
            print("Identidade inválida!")


p1 = Pessoa("Maria", "01/01/2000", "12345678901", "MG12345")

print("Nome:", p1.nome)
print("Data de nascimento:", p1)
