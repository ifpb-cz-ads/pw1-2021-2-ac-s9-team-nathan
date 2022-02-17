class Televisao:
    def __init__(self,marca,tamanho):
        self.ligada = False
        self.canal = 2
        self.marca = marca
        self.tamanho = tamanho

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv = Televisao('SepmThoshiba','60p')
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
tv1 = Televisao('Samsung','40p')
tv2 = Televisao('LG','50p')
print(tv1.marca)
print(tv1.tamanho)
print(tv2.marca)
print(tv2.tamanho)
