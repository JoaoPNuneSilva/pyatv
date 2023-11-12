# Crie uma classe Curso que contém os
# atributos nome e duracao (em
# anos). Em seguida, crie duas subclasses: Presencial e Online. A classe
# Presencial deve ter um atributo adicional chamado numero_de_vagas e a
# classe Online deve ter um atributo adicional chamado plataforma_online.
# Utilize o método super() para inicializar os atributos herdados da classe Curso
# nas subclasses. Sobrescreva um método chamado detalhes_do_curso em
# cada subclasse, de modo que ele retorne uma string
# contendo todas as informações do curso, incluindo os atributos específicos de
# cada subclasse. Por fim, crie instâncias das subclasses Presencial e Online e
# imprima as informações de cada curso usando o método detalhes_do_curso.
class Curso:
    def __init__(self, nome, duracao, instituicao):
        self.nome = nome
        self.duracao = duracao
        self.instituicao = instituicao
    
    def detalhes_do_curso(self):
        return f"Nome: {self.nome}\nDuração: {self.duracao} anos\nInstituição: {self.instituicao}"

class Presencial(Curso):
    def __init__(self, nome, duracao, instituicao, numero_de_vagas):
        super().__init__(nome, duracao, instituicao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nNúmero de Vagas: {self.numero_de_vagas}"
    

class Online(Curso):
    def __init__(self, nome, duracao, instituicao, plataforma_online):
        super().__init__(nome, duracao, instituicao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nPlataforma Online: {self.plataforma_online}"

curso_presencial = Presencial("Análise e Desenvolvimento de Sistemas", 2, "UNIVALE", 35)
curso_online = Online("Ilustração", 4, "EBAC","Aulas gravadas disponibilizadas na plataforma da instituição")

print(f"Informações do Curso {curso_presencial.nome}")
print(curso_presencial.detalhes_do_curso())

print(f"\nInformações do Curso {curso_online.nome}")
print(curso_online.detalhes_do_curso())