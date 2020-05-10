from empregado import Empregado


class Adm(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self._ajuda_de_custo = ajuda_de_custo

    @property
    def ajuda_de_custo(self):
        return self._ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, valor):
        if valor >= 0:
            self._ajuda_de_custo = valor

    def calcular_salario(self):
        return super().calcular_salario() + self.ajuda_de_custo
