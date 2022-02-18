class Estado:
    def __init__(self,nome,sigla,cidades,populacao):
        self.nome=nome
        self.sigla=sigla
        self.cidades=cidades
        self.populacao=populacao
class Cidade:
    def __init__(self,nome,populacao):
        self.nome=nome
        self.populacao=populacao
a = Cidade('Cajazeiras',20)
b = Cidade('Santa Helena',50)
c = Cidade('Sao Jose de Piranhas',90)
cidades = [a.nome,b.nome,c.nome]
estado_a_p = (a.populacao) + (b.populacao) + (c.populacao)
Estado_A= Estado('Paraiba','PB',cidades,estado_a_p)
print(Estado_A.cidades)
print(Estado_A.populacao)
d = Cidade('Sao Paulo',2000)
e = Cidade('Campinas',5000)
f = Cidade('Campos do Jordao',7000)
cidades = [d.nome,e.nome,f.nome]
estado_b_p = (d.populacao) + (e.populacao) + (f.populacao)
Estado_B= Estado('Sao Paulo','SP',cidades,estado_b_p)
print(Estado_B.cidades)
print(Estado_B.populacao)
g = Cidade('Rio de Janeiro',239412)
h = Cidade('Volta Redonda',98123)
i = Cidade('Niteroi',9123112)
cidades = [g.nome,h.nome,i.nome]
estado_c_p = (g.populacao) + (h.populacao) + (i.populacao)
Estado_C= Estado('Rio de Janeiro','RJ',cidades,estado_c_p)
print(Estado_C.cidades)
print(Estado_C.populacao)