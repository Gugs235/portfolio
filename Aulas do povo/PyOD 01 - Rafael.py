from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    idade: int
    email: str
Usuario = Usuario(nome='João', idade=54, email='joao@exemplo.com')
print(Usuario.nome)
print(Usuario.idade)
print(Usuario.email)

class Usuario1(BaseModel):
    nome: str
    sexo: str
    idade: int
Usuario1 = Usuario1(nome= "jhonathan", idade=16 , sexo='masc')
print(Usuario1.nome)
print(Usuario1.idade)
print(Usuario1.sexo)
