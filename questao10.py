class Conta:
    def __init__(self, clientes, número, saldo=0,telefone=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)
        self.telefone=telefone

    def resumo(self):
        print("CC N°%s Saldo: %10.2f  Telefone: %s" %
              (self.número, self.saldo,self.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            self.operações.append(["Saldo Insuficiente"])
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            return False
    def extrato(self):
        saldoTotal = self.saldo + self.limite
        print("Extrato CC N° %s \n O saldo total disponivel para saque e: %.2f \n  O limite e de : %.2f \n" % (self.número,saldoTotal,self.limite))
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)
c1 = ContaEspecial('Maria',678,200,800)
c1.extrato()