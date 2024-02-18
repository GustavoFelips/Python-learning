class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = 0

    def saque(self,valor):
        if valor > self._saldo:
            print("Saldo insuficiente")
        else:
            self._saldo = self._saldo - valor

    def deposito(self,valor):
        self._saldo = self._saldo + valor

    def extrato(self):
        return (f"Nome : {self._titular} , Conta : {self._numero}, Saaldo : {self._saldo}")

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        if saldo < 0 :
            print("Não pode número negativo")
        else:
            self._saldo = saldo
