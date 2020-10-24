class Egresos:
    def _init_(self, saldoInicial, egreso):
        self.__saldoInicial = saldoInicial
        self.__egreso = egreso

    def Add(self):
        resultEgreso = self._saldoInicial - self._egreso
        return resultEgreso