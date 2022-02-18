class Televisao:
    def __init__(self,marca,tamanho,canal,canalMax = 14,canalMin = 2):
        self.ligada = False
        self.canal = canal
        self.canalMax=canalMax
        self.canalMin=canalMin
        self.marca = marca
        self.tamanho = tamanho

    def muda_canal_para_baixo(self):
        if self.canal <= self.canalMin:
            self.canal = self.canalMax
        else:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal >= self.canalMax:
            self.canal = self.canalMin
        else:
            self.canal += 1
tv1=  Televisao('LG','40P',2,4,1)
print(tv1.canalMax)
print(tv1.canalMin)
tv2=  Televisao('LG','40P',2)
print(tv2.canalMax)
print(tv2.canalMin)
