# Programação Orientada a Objetos: Gestão de Acervo Para modernizar a biblioteca corporativa, foi solicitada a criação da classe base de gerenciamento de livros do acervo utilizando os conceitos fundamentais de Orientação a Objetos em Python, sem herança.
# ● Regras de Negócio e Requisitos da Classe Livro:
# ○ Atributos de Instância: No construtor (__init__), inicialize: titulo (str), autor (str),
# ano_publicacao (int) e disponivel (bool, padrão True).
# ○ Métodos da Classe: Implementar os seguintes métodos com validação do estado do
# objeto:
# i. emprestar(): se disponível, altera para False e emite sucesso; se já emprestado,
# emite aviso de indisponibilidade;
# ii. devolver(): se emprestado, altera para True e confirma devolução; se já disponível,
# avisa que não constava como emprestado;
# iii. exibir_ficha_tecnica(): imprime de forma organizada os dados do exemplar (Título,
# Autor, Ano e Situação: 'Disponível' ou 'Emprestado').

# ○ Bateria de Testes:
# i. instanciar pelo menos 2 livros distintos e executar a sequência:
# ii. exibição das fichas iniciais;
# iii. empréstimo do livro 1;
# iv. tentativa de novo empréstimo do livro 1 (validando a trava);
# v. devolução do livro 1;
# vi. exibição das fichas finais atualizadas.
# Restrição Técnica: Proibido o uso de herança neste momento. Manter a consistência do atributo
# self.disponivel através dos métodos.





# Regras de Negócio e Requisitos da Classe Livro
# Restrição Técnica: Proibido o uso de herança neste momento.
# Manter a consistência do atributo self.disponivel através dos métodos.



class livro:
    # Atributos de Instância: No construtor (__init__), inicialize:
    # titulo (str), autor (str), ano_publicacao (int) e disponivel (bool, padrão True).
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  # Inicialmente, o livro está disponível


    # Métodos da Classe:
    # i. emprestar(): se disponível, altera para False e emite sucesso;
    # se já emprestado, emite aviso de indisponibilidade;

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Sucesso: O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"Aviso: O livro '{self.titulo}' está indisponível (já se encontra emprestado).")

    # ii. devolver(): se emprestado, altera para True e confirma devolução;
    # se já disponível, avisa que não constava como emprestado;

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Sucesso: A devolução do livro '{self.titulo}' foi confirmada.")
        else:
            print(f"Aviso: O livro '{self.titulo}' já está disponível e não constava como emprestado.")




    # iii. exibir_ficha_tecnica(): imprime de forma organizada os dados do exemplar
    # (Título, Autor, Ano e Situação: 'Disponível' ou 'Emprestado')

    def exibir_ficha_tecnica(self):
        situacao = "Disponível" if self.disponivel else "Emprestado"
        print("-" * 45)
        print(f"Título:   {self.titulo}")
        print(f"Autor:    {self.autor}")
        print(f"Ano:      {self.ano_publicacao}")
        print(f"Situação: {situacao}")
        print("-" * 45)


#bateria de testes
if __name__ == "__main__":
    # Instanciando dois livros distintos
    livro1 = livro("1984", "George Orwell", 1949)
    livro2 = livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

    # Exibição das fichas iniciais
    print("=== FICHAS TÉCNICAS INICIAIS ===")
    livro1.exibir_ficha_tecnica()
    livro2.exibir_ficha_tecnica()

    # Empréstimo do livro 1
    print("\n=== EMPRÉSTIMO DO LIVRO 1 ===")
    livro1.emprestar()

    # Tentativa de novo empréstimo do livro 1 (validando a trava)
    print("\n=== TENTATIVA DE NOVO EMPRÉSTIMO DO LIVRO 1 ===")
    livro1.emprestar()

    # Devolução do livro 1
    print("\n=== DEVOLUÇÃO DO LIVRO 1 ===")
    livro1.devolver()

    # Exibição das fichas finais atualizadas
    print("\n=== FICHAS TÉCNICAS FINAIS ATUALIZADAS ===")
    livro1.exibir_ficha_tecnica()
    livro2.exibir_ficha_tecnica()

