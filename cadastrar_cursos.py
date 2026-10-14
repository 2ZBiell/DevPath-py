from app.database import Tabela_Cursos, InserirCurso

Tabela_Cursos()

cursos = [
    (
        "Python 3",
        "Curso em Vídeo",
        "Python",
        "Curso introdutório sobre variáveis, condicionais, "
        "laços de repetição e funções.",
        1
    ),
    (
        "Python para Iniciantes",
        "freeCodeCamp",
        "Python",
        "Introdução à linguagem Python e à programação ",
        1
    ),
    (
        "Programação em C++",
        "Corujinhas",
        "C++",
        "Curso livre voltado ao aprendizado da linguagem C++"
        "abordando conceitos de programação e conteúdos para"
        "desenvolver lógica e criar programas.",
        1
    ),
    (
        "Java para iniciantes",
        "CURSA",
        "Java",
        "Ensina Java desde os primeiros programas até estruturas"
        "de repetição, vetores e métodos. É indicado para quem está"
        "começando.",
        1
    )
]

for curso in cursos:
    InserirCurso(*curso)

print("Cursos cadastrados!")
