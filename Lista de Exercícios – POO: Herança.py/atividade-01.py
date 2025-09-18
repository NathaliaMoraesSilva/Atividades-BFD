#1Crie uma classe Usuario 
#com atributos nome e email.
#Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email= email
us1 = Usuario("João","João@hotmail.com")
print(us1.nome)
print(us1.email)
class Cliente:
    def __init__(self,nome,email):
        super().__init__(nome,email)
        
cliente1=Cliente("João",24)

    
        
        
        
        
