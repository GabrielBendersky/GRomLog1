class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self._nota = 0.0  # Valor padrão seguro caso a nota inicial seja rejeitada
        self.nota = nota  # Aciona o @nota.setter já na criação do objeto

    @property
    def nota(self) -> float:
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if 0.0 <= valor <= 10.0:
            self._nota = float(valor)
        else:
            print(f"Erro: A nota {valor} é inválida. O valor deve estar entre 0.0 e 10.0.")

    @property
    def aprovado(self) -> bool:
        return self._nota >= 6.0


# Exemplos de uso e validação:
aluno1 = Aluno("Mariana", 8.5)
print(f"Aluno: {aluno1.nome} | Nota: {aluno1.nota} | Aprovado: {aluno1.aprovado}")

# Tentativas inválidas (são bloqueadas e a nota anterior permanece intacta)
aluno1.nota = -5
aluno1.nota = 150
print(f"Nota após tentativas inválidas: {aluno1.nota}")

# Atualização válida abaixo da média
aluno1.nota = 5.5
print(f"Nota atualizada: {aluno1.nota} | Aprovado: {aluno1.aprovado}")

# Teste instanciando com nota inválida
aluno2 = Aluno("Lucas", 12.0)
print(f"Aluno: {aluno2.nome} | Nota: {aluno2.nota} | Aprovado: {aluno2.aprovado}")
