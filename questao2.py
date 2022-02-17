class Televisao:
    def __init__(self,marca,tamanho,canal):
        self.ligada = False
        self.canal = canal
        self.marca = marca
        self.tamanho = tamanho

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1
tv1=  Televisao('LG','40P','1')
print(tv1.canal)
