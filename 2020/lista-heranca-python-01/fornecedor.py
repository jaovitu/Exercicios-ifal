from pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, telefone)
        self._valor_credito = valor_credito
        self._valor_divida = valor_divida

    @property
    def valor_credito(self):
        return self._valor_credito

    @valor_credito.setter
    def valor_credito(self, valor):
        self._valor_credito = valor

    @property
    def valor_divida(self):
        return self._valor_divida

    @valor_divida.setter
    def valor_divida(self, valor):
        if valor > 0:
            self._valor_divida = valor

    def obter_saldo(self):
        return self.valor_credito - self.valor_divida
