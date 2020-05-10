from pessoa import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, endereco, telefone)
        self._codigo_setor = codigo_setor
        self._salario_base = salario_base
        self._imposto = imposto

    @property
    def codigo_setor(self):
        return self._codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo):
        self._codigo_setor = codigo

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario):
        if salario > 0:
            self._salario_base = salario

    @property
    def imposto(self):
        return self._imposto

    @imposto.setter
    def imposto(self, imposto):
        if 0 <= imposto <= 100:
            self._imposto = imposto

    def calcular_salario(self):
        return self.salario_base - (self.imposto / 100 * self.salario_base)
