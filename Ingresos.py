class Ingresos:
    def _init_(self, saldoInicial, ingreso):
        self.__saldoInicial = saldoInicial
        self.__ingreso = ingreso

    def Add(self):
        resultIngreso = self._saldoInicial + self._ingreso
        return resultIngreso