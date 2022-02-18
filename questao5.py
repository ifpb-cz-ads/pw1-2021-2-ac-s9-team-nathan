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
    def set_canalMax(self,canalMax):
        self.canalMax=canalMax
    def set_canalMin(self,canalMin):
        self.canalMin=canalMin

tv1=  Televisao('LG','40P',4)
print(tv1.canalMax)
print(tv1.canalMin)
tv1.set_canalMin(4)
tv1.set_canalMax(15)
print(tv1.canalMax)
print(tv1.canalMin)
tv2=  Televisao('Samsung','70p',2)
print(tv2.canalMax)
print(tv2.canalMin)
tv2.set_canalMin(9)
tv2.set_canalMax(20)
print(tv2.canalMax)
print(tv2.canalMin)