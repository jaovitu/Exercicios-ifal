from empregado import Empregado


class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_producao, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self._valor_producao = valor_producao
        self._comissao = comissao

    @property
    def valor_producao(self):
        return self._valor_producao

    @valor_producao.setter
    def valor_producao(self, valor):
        if valor >= 0:
            self._valor_producao = valor

    @property
    def comissao(self):
        return self._comissao

    @comissao.setter
    def comissao(self, comissao):
        if 0 <= comissao <= 100:
            self._comissao = comissao

    def calcular_salario(self):
        return super().calcular_salario() + (self.comissao / 100 * self.valor_producao)
