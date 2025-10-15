from abc import ABC, abstractmethod
# 4-Forçando contrato
# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id).
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos.
# O que acontece quando você tenta instanciá-la?
# Corrija o código.

# 1 Definição da interface
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# Subclasse concreta implementando todos os métodos
class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        self.dados[objeto['id']] = objeto
        print(f"Objeto {objeto} salvo na memória")

    def buscar(self, id):
        return self.dados.get(id, None)

# Testando
repo = RepositorioMemoria()
repo.salvar({'id': 1, 'nome': 'Teste'})
print(repo.buscar(1))
